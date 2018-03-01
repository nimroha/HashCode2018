import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, R, C, T):

        dg = nx.DiGraph()
        for t in range(T):
            for c in range(C):
                for r in range(R):
                    dg.add_node((r, c, t))

        for node in dg.nodes:

            if node[2] < T - 1:
                dg.add_edge(node, (node[0], node[1], node[2] + 1))
                if node[1] + 1 < C:
                    dg.add_edge(node, (node[0], node[1] + 1, node[2] + 1))
                if node[1] > 0:
                    dg.add_edge(node, (node[0], node[1] - 1, node[2] + 1))
                if node[0] + 1 < R:
                    dg.add_edge(node, (node[0] + 1, node[1], node[2] + 1))
                if node[0] > 0:
                    dg.add_edge(node, (node[0] - 1, node[1], node[2] + 1))

        # nx.draw(dg)
        # plt.show()
        self.dg = dg
