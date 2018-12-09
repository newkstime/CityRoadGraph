from comparable import Comparable

class Edge(Comparable):
    """
    This class represents a Edge on a graph
    Instance variables:
            self.from_vertex: Vertex
            self.to_vertex: Vertex
            self.weight: int
    """

    def __init__(self, from_vertex, to_vertex, weight=0):
        """
        Create a new edge object with the passed in vertices and weight
        """
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def set_weight(self, weight):
        """
        Sets the weight
        """
        self.weight = weight

    def get_weight(self):
        """
        Return the weight
        """
        return self.weight

    def compare(self, other_edge):
        """
        Compares weights
        """
        return self.weight - other_edge.weight

    def __str__(self):
        """
        Returns a string representation of the Edge
        """
        return (str(self.from_vertex) + " : " +
                str(self.to_vertex) + " : " + str(self.weight))
