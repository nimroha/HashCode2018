import src.TLayer as TLayer


class Graph:

    def __init__(self, R, C, T):

        self.graph = None

        for t in range(T):

            layer = TLayer(R, C, t)
            self.graph =