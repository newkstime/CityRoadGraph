from graphTree import GraphTree
class ShortestPathTree(GraphTree):
    """
    This class presents a tree for storing the order of the vertices
    producing the shortest path through the weighted graph vertices
    """ 
    def __init__(self, root, search_order, parents, cost, wertices):
        """
        Create shortest path tree
        Instance variable: cost: Python list
        """
        super().__init__(root, search_order, parents)
        self.cost = cost
        self.vertices = wertices

    def get_cost(self, vertex):
        """
        Return the cost for a path from the root to vertex 
        """
        for index in range(len(self.vertices)):
            if self.vertices[index].get_name() == vertex.get_name(): 
                 cost_index = index
        return self.cost[cost_index]

    def get_all_paths_str(self):
        """
        Create a string containing all the shortest paths
        from all vertices to the root
        """
        root_name = self.get_root().get_name()
        path_str = "All shortest paths from " + root_name + " are: \n"

        for index in range(len(self.cost)):
            path_str += self.get_vert_str(self.vertices[index])
            path_str += " (Cost: " + self.cost[index] + ")\n"
        return path_str
