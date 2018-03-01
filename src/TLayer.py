import networkx as nx
import matplotlib.pyplot as plt

class TLayer:

    def __init__(self, R, C, t):

        dg = nx.DiGraph()
        for c in range(C):
            for r in range(R):
                dg.add_node((r, c, t))

        for node in dg.nodes:

            if node[1] + 1 < C:
                dg.add_edge(node, (node[0], node[1] + 1, t))
            if node[1] > 0:
                dg.add_edge(node, (node[0], node[1] - 1, t))
            if node[0] + 1 < R:
                dg.add_edge(node, (node[0] + 1, node[1], t))
            if node[0] > 0:
                dg.add_edge(node, (node[0] - 1, node[1], t))

        # nx.draw(dg)
        # plt.show()
        self.dg = dg
