import networkx as nx
from networkx import NetworkXNoPath
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, R, C, T):

        dg = nx.DiGraph()
        for t in range(T):
            for c in range(C):
                for r in range(R):
                    dg.add_node((r, c, t))

        dg.add_node('end')
        for node in dg.nodes:

            if node[2] < T - 1:

                dg.add_edge(node, (node[0], node[1], node[2] + 1), weight=1)
                if node[1] + 1 < C:
                    dg.add_edge(node, (node[0], node[1] + 1, node[2] + 1), weight=1)
                if node[1] > 0:
                    dg.add_edge(node, (node[0], node[1] - 1, node[2] + 1), weight=1)
                if node[0] + 1 < R:
                    dg.add_edge(node, (node[0] + 1, node[1], node[2] + 1), weight=1)
                if node[0] > 0:
                    dg.add_edge(node, (node[0] - 1, node[1], node[2] + 1), weight=1)

            else:
                dg.add_edge(node, 'end', weight=0)

        # nx.draw(dg)
        # plt.show()
        self.dg = dg

    def remove_rides(self, ride_schedule):
        # TODO
        pass

    def find_shortest_path(self):
        try:
            path = nx.dijkstra_path(self.dg, (0,0,0), 'end')
        except NetworkXNoPath:
            path = []
        return path