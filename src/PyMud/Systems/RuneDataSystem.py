from Systems.system import System
from spells.runes import runes
from itertools import dropwhile


class CreateRuneData(System):
    manditory = ['runes']
    optional = ['rune_data']

    def lookup(self, id):
        return runes[id]

    def newest(self, current, new):
        return dropwhile(lambda c: c[0] == c[1], zip(new, current))

    def handle(self, node):
        if not node.has('rune_data'):
            runes = []
            for id in node.runes.runes_list:
                rn_cls = self.lookup(id)
                rn = rn_cls(self.node_factory)
                runes.append(rn)
            node.add_component(
                'rune_data', {'runes': runes, 'covered': node.runes.runes_list})
        else:
            # print(node.rune_data.covered, node.runes.runes_list)
            for new, _ in self.newest(node.rune_data.covered, node.runes.runes_list):
                rn_cls = self.lookup(new)
                rn = rn_cls(self.node_factory)
                node.rune_data.runes.append(rn)
            node.rune_data.covered = node.runes.runes_list
