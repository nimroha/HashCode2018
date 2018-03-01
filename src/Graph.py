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

        dg.add_node((0,0,T))
        for node in dg.nodes:
            r, c, t = node
            if t < T - 1:

                dg.add_edge(node, (r, c, t + 1), weight=1)
                if c + 1 < C:
                    dg.add_edge(node, (r, c + 1, t + 1), weight=1)
                if c > 0:
                    dg.add_edge(node, (r, c - 1, t + 1), weight=1)
                if r + 1 < R:
                    dg.add_edge(node, (r + 1, c, t + 1), weight=1)
                if r > 0:
                    dg.add_edge(node, (r - 1, c, t + 1), weight=1)

            else:
                dg.add_edge(node, (0,0,T), weight=0)

        # nx.draw(dg)
        # plt.show()
        self.dg = dg

    def remove_rides(self, ride_schedule):
        # TODO
        pass

    def find_shortest_path(self, end):
        try:
            path_of_nodes = nx.dijkstra_path(self.dg, (0,0,0), end)
            path_of_edges = []
            for i in range(len(path_of_nodes) - 1):
                edge = (path_of_nodes[i], path_of_nodes[i+1])
                path_of_edges.append(edge)
        except NetworkXNoPath as e:
            print(e)
            path_of_edges = []

        return path_of_edges
