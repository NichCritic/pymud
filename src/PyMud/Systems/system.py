class System(object):
    manditory = []
    optional = []
    handles = []

    def __init__(self, node_factory):
        self.node_factory = node_factory

    def process(self):
        for node in self.get_nodes():
            # print(f"{self.__class__.__name__} system got message from
            # {node.id}")
            self.handle(node)
            self.clean(node)

    def handle(self, node):
        pass

    def clean(self, node):
        [node.remove_component(c) for c in self.handles]

    def get_nodes(self):
        return self.node_factory.create_node_list(self.manditory,
                                                  self.optional)
