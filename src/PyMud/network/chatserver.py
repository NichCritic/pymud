#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import tornado.auth
import tornado.escape

import tornado.web

import uuid

from tornado import gen
from tornado.options import define


define("port", default=8888, help="run on the given port", type=int)


class MessageBuffer(object):

    def __init__(self):
        self.waiters = set()
        self.cache = []
        self.cache_size = 200

    def wait_for_messages(self, callback, cursor=None):
        if cursor:
            new_count = 0
            for msg in reversed(self.cache):
                if msg["id"] == cursor:
                    break
                new_count += 1
            if new_count:
                callback(self.cache[-new_count:])
                return
        self.waiters.add(callback)

    def cancel_wait(self, callback):
        self.waiters.remove(callback)

    def new_messages(self, messages):
        logging.info("Sending new message to %r listeners", len(self.waiters))
        for callback in self.waiters:
            try:
                callback(messages)
            except:
                logging.error("Error in waiter callback", exc_info=True)
        self.waiters = set()
        self.cache.extend(messages)
        if len(self.cache) > self.cache_size:
            self.cache = self.cache[-self.cache_size:]


# Making this a non-singleton is left as an exercise for the reader.
#global_message_buffer = MessageBuffer()
#user_message_buffers = data_cache.user_message_buffers


class BaseHandler(tornado.web.RequestHandler):

    def create_player(self):
        with self.session_manager.get_session() as session:
            player = self.player_factory.create_player(
                MessageBuffer(), self.current_user["id"])
            self.current_user["player_id"] = player.id
            avatar_id = self.account_utils.get_previous_avatar_for_player(
                player.id, session)
            if avatar_id is None:
                self.redirect("/charater_select")
                return
            self.player_factory.set_player_avatar(player, avatar_id)

    def get_current_user(self):
        user_json = self.get_secure_cookie("chatdemo_user")
        if not user_json:
            return None
        # return {"name": "Nicholas", "email": "n.aelick@gmail.com", "id":
        # "11111", "given_name": 'Nicholas', "acct_id": 1, "player_id":
        # "11111"}
        return tornado.escape.json_decode(user_json)


class MainHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.render("index.html", messages=[])


class CharacterCreateHandler(BaseHandler):

    def initialize(self, account_utils, player_factory, session_manager):
        self.account_utils = account_utils
        self.player_factory = player_factory
        self.session_manager = session_manager

    @tornado.web.authenticated
    def get(self):
        self.render("character_create.html")

    @tornado.web.authenticated
    def post(self):
        # print(self.current_user)
        acct_id = self.current_user["acct_id"]

        # print(self.current_user)
        print(self.request.body)

        post_data = self.request.body.decode('utf-8')

        post_data = post_data.split('&')

        post_data = dict([p.split('=') for p in post_data])

        data = {"name": post_data['character_name']}

        with self.session_manager.get_session() as session:
            self.account_utils.create_new_avatar_for_account(
                acct_id, data, session)

        # print(self.request.body)
        self.write({"result": "ok"})
        self.finish()
        # if self.get_argument("next", None):
        #    self.redirect(self.get_argument("next"))


class CharacterSelectHandler(BaseHandler):

    def initialize(self, account_utils, player_factory, node_factory, session_manager):
        self.account_utils = account_utils
        self.player_factory = player_factory
        self.node_factory = node_factory
        self.av = None
        self.session_manager = session_manager

    @tornado.web.authenticated
    def get(self):
        with self.session_manager.get_session() as session:
            acc_id = self.current_user["acct_id"]
            acc = self.account_utils.get_by_id(acc_id, session)
            avatars = acc.avatars

            if not self.current_user['id'] in self.player_factory.players:
                player = self.player_factory.create_player(
                    MessageBuffer(), self.current_user["id"])
                self.current_user["player_id"] = player.id

            self.av = []

            for i, avatar in enumerate(avatars):
                id = avatar.avatar_id
                avatar_node = self.node_factory.create_node(
                    id, ['names', 'location'], ['player_controlled'])
                name = avatar_node.names.name
                location_node = self.node_factory.create_node(
                    avatar_node.location.room, ['names'])
                location = location_node.names.name
                description = "temp_description"

                if avatar_node.has('player_controlled'):
                    avatar_node.remove_component('player_controlled')

                self.av.append({
                    "index": i,
                    "id": id,
                    "name": name,
                    "location": location,
                    "description": description
                })

            self.render("character_select.html", characters=self.av)

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        # print(self.request.body)
        with self.session_manager.get_session() as session:
            # import pdb; pdb.set_trace()
            player = self.player_factory.get_player(
                self.current_user["player_id"])

            index = self.get_argument("id")

            acc_id = self.current_user["acct_id"]
            acc = self.account_utils.get_by_id(acc_id, session)
            avatars = self.account_utils.get_avatars_for_account(acc, session)

            # print(avatars)

            self.av = [{"index": index, "id": av.avatar_id}
                       for index, av in enumerate(avatars)]

            self.player_factory.set_player_avatar(
                player, self.av[int(index)]["id"])
            # TODO: messy hack
            self.account_utils.set_avatars_pid(
                self.av[int(index)]["id"], player.id, session)

            if self.get_argument("next", None):
                self.redirect(self.get_argument("next"))
            else:
                self.write(tornado.escape.to_basestring("ok"))
                self.finish()

        # if self.get_argument("next", None):
        #    self.redirect(self.get_argument("next"))


class CommandMessageHandler(BaseHandler):

    def initialize(self, command_handler, player_factory, session_manager, account_utils):
        self.command_handler = command_handler
        self.player_factory = player_factory
        self.session_manager = session_manager
        self.account_utils = account_utils

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        message = {
            "id": str(uuid.uuid4()),
            "from": self.current_user["given_name"],
            "body": self.get_argument("body"),
        }
        logging.info(self.current_user)
        if not self.current_user['id'] in self.player_factory.players:
            self.create_player()
        player = self.player_factory.get_player(self.current_user["player_id"])
        result = self.command_handler.handle_command(player, message["body"])
        logging.info(result)
        if result[0] == "error":
            # to_basestring is necessary for Python 3's json encoder,
            # which doesn't accept byte strings.
            message["body"] = ["Sorry, I can't understand that"]
        else:
            message["body"] = [""]
        message["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=message))
        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)
        self.player_factory.players[self.current_user[
            "id"]].message_buffer.new_messages([message])
        self.finish()


class MessageUpdatesHandler(BaseHandler):

    def initialize(self, player_factory, account_utils, session_manager, node_factory):
        # TODO: This seems strange
        self.player_factory = player_factory
        self.account_utils = account_utils
        self.session_manager = session_manager
        self.node_factory = node_factory

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        print(self.current_user["id"])
        cursor = self.get_argument("cursor", None)
        if not self.current_user['id'] in self.player_factory.players:
            self.create_player()

        self.player_factory.players[self.current_user["id"]].message_buffer.wait_for_messages(self.on_new_messages,
                                                                                              cursor=cursor)

    def on_new_messages(self, messages):
        # Closed client connection
        if self.request.connection.stream.closed():
            return
        with self.session_manager.get_session():
            avatar_id = self.player_factory.players[
                self.current_user["id"]].avatar_id
            avatar = self.node_factory.create_node(
                avatar_id, ["health", "mana"])
            health = avatar.health.health
            max_health = avatar.health.max_health
            mana = avatar.mana.mana
            max_mana = avatar.mana.max_mana

        self.finish(dict(
            messages=messages,
            health=health,
            max_health=max_health,
            mana=mana,
            max_mana=max_mana
        ))

    def on_connection_close(self):
        self.player_factory.players[self.current_user[
            "id"]].message_buffer.cancel_wait(self.on_new_messages)


class AuthLoginHandler(BaseHandler, tornado.auth.GoogleOAuth2Mixin):

    def initialize(self, account_utils, player_factory, session_manager):
        self.account_utils = account_utils
        self.player_factory = player_factory
        self.session_manager = session_manager

    @gen.coroutine
    def get(self):
        print(self.get_query_argument("code", False))
        if self.get_query_argument("code", False):

            access = yield self.get_authenticated_user(
                redirect_uri='http://naelick.com:8888/auth/login',
                code=self.get_query_argument('code'))
            user = yield self.oauth2_request(
                "https://www.googleapis.com/oauth2/v1/userinfo",
                access_token=access["access_token"])
            print(user)
            with self.session_manager.get_session() as session:

                acct = self.account_utils.handle_login(
                    user, self.player_factory, session)
                player = self.player_factory.create_player(
                    MessageBuffer(), user["id"])

                user["acct_id"] = acct.id
                user["player_id"] = player.id

                self.set_secure_cookie("chatdemo_user",
                                       tornado.escape.json_encode(user))

                self.redirect("/character_select")
                return
        self.authorize_redirect(
            redirect_uri='http://naelick.com:8888/auth/login',
            client_id="746170306889-840qspkc0dcdlb3sur4ml7daalll4uvo.apps.googleusercontent.com",
            scope=['email'],
            response_type='code',
            extra_params={'approval_prompt': 'auto'})


class AuthLogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie("chatdemo_user")
        self.render('logout.html')
