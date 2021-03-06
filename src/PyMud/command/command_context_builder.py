'''
Created on 2013-11-18

@author: Nich
'''
class CommandContextBuilder(object):
    
    def __init__(self, node_factory, runes, verbs):
        self.node_factory = node_factory
        self.runes = runes
        self.verbs = verbs
    
    def build_command_context(self, source):
        avatar_id = source.avatar_id
        node = self.node_factory.create_node(avatar_id, ["location", "names", "visible_names"])
        command_context = {"player_node":node,
                           "calling_player_id":avatar_id,
                                "calling_player_location": node.location,
                                "names":node.visible_names,
                                "runes": self.runes,
                                "verbs": self.verbs
                           }
        
        
        
        return command_context