# Fireballs are a projectile which does damage with the fire element
# Practically speaking, the fire element should just provoke a large change
# in temperature and let that system decide what to do


def fireball(target):

    target.add_component('projectile', {
        'on_hit': set_on_fire,
        'on_miss': do_miss,
        'on_attach': incoming_fireball,
        'timeout': 3,  # Todo: should do some math on timeout rules and set this as a policy
        'args': {}
    })


def set_on_fire(target):
    target.add_or_update_component('on_fire', {'duration': 5})


def do_miss(target):
    # need to do some av work here. Naively we can get the target's room and create the event, but it's really annoying to do this every time
    # Actually we can't even, because we'd need a node factory. It would be nice if objects can emit events directly
    # That's not hard to do though

    # target.add_or_attach_component('av_event': {format:[yadda yadda]})

    # Then have a system that picks this up and tosses it up to the nearest
    # room. Then we can do av_events almost as easily as network messages
    pass


def on_attach()
