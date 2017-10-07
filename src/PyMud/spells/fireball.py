# Fireballs are a projectile which does damage with the fire element
# Practically speaking, the fire element should just provoke a large change
# in temperature and let that system decide what to do


def fireball_hit(target, player):

    thing = 'fireball'
    effect = 'setting {who} on fire'

    target.add_or_attach_component('av_event': {'format': [
        ([("visibility", 60), ("is_target")], [
         "The {thing} strikes {who}, {effect}."]),
        ([("visibility", 60)], [
         "The fireball strikes {target}, setting them on fire."]),
    ], 'data': {'target': target.names.name, 'player': player.names.name}})
    target.add_or_update_component('on_fire', {'duration': 5})


def fireball_miss(target, player):
    # need to do some av work fireball_attach. Naively we can get the target's room and create the event, but it's really annoying to do this every time
    # Actually we can't even, because we'd need a node factory. It would be nice if objects can emit events directly
    # That's not hard to do though

    target.add_or_attach_component('av_event': {'format': [
        ([("visibility", 60), ("is_target")], [
         "You jump out of the way of {player}'s fireball"]),
        ([("visibility", 60), ("is_caller")], [
         "{target} jumps out of the way of your fireball"]),
        ([("visibility", 60)], [
         "{target} jumps out of the way of {player}'s fireball"]),
    ], 'data': {'target': target.names.name, 'player': player.names.name}})


def fireball_attach(target, player):
    target.add_or_attach_component('av_event': {'format': [
        ([("visibility", 60), ("is_target")], [
         "A fireball streaks from {player}'s outstretched hands towards you"]),
        ([("visibility", 60), ("is_caller")], [
         "A fireball streaks from your hands towards {target}"]),
        ([("visibility", 60)], [
         "A fireball streaks from {player}'s outstretched hands towards {target}"]),
    ], 'data': {'target': target.names.name, 'player': player.names.name}})


fireball_spec = {
    'on_hit': fireball_hit,
    'on_attach': fireball_attach,
    'on_miss': fireball_miss,
}


def ball(source, target, spec):

    target.add_component('projectile', {
        'on_hit': spec['on_hit'],
        'on_miss': spec['on_miss'],
        'on_attach': spec['on_attach'],
        'timeout': 3,  # Todo: should do some math on timeout rules and set this as a policy
        'args': {'target': target, 'player': source}
    })
