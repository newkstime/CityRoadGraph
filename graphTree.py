class GraphTree:
    """
    This class represents trees used with graphs.
    These trees hold spanning trees created via a graph traversal.
    Both depth-first search (DFS) and breadth-first search
    (BFS) graph traversals produce spanning trees.
    There are algorithms for finding minimum spanning trees (MSTs)
    of a graph and the shortest path between vertices in a graph.  
    These spanning trees and paths are stored in GraphTrees.
    Each node in the tree is a vertex from the graph.
    There are three instance variables for this GraphTree.
    1. The vertices are stored in a Python list called 
       search_order as they are visited by the traversal.  
    2. The parent vertices for the vertices in the traversal are 
       also stored in a Python list called parents.
    3. The root of the tree.
    """
    def __init__(self, root, search_order, parents):
        """
        Creates a GraphTree used with graph traversals
        The instance variables are:
           root: The root of the tree: starting vertex
           search_order: Python list of vertices in visit order
           parents: Python list of parents of the vertices
        """
        self.root = root
        self.search_order = search_order
        self.parents = parents

    def get_root(self):
        """
        Return the root of the tree
        """
        return self.root

    def get_parent(self, vertex): 
        """
        Return the parent of the given vertex
        """
        index = vertex.get_index()
        return self.parents[index]

    def get_search_order(self):
        """
        Return the list representing the search order
        """
        return self.search_order

    def get_num_verts_found(self):
        """
        Return the number of vertices in the search order
        """
        return len(self.search_order)
         
    def get_path(self, vertex):
        """
        Return the path of vertices from a given vertex to the root
        """
        path = []
        root_name = self.root.get_name()
        curr_vertex = vertex
        while curr_vertex.get_name() != root_name:
            path.append(curr_vertex)
            curr_vertex = self.get_parent(curr_vertex)
        return path

    def get_vert_str(self, vertex):
        """
        Return a string holding path of vertices 
        from the root to the given vertex
        """
        path = self.get_path(vertex)
        path.reverse()
        path_str = "A path from " + str(self.root) + " to " + str(vertex) + ": \n"
        node_count = 0
        for vert in path:
            if node_count % 5 == 0:
                path_str += "\n"
            path_str += str(vert) + " --> "    
            node_count += 1

        return path_str

    def get_edge_str(self, vertices):
        """
        Return a string holding path of edges from the root
        to the starting vertex given when the tree was built
        """
        path_str = "Root is  " + str(self.root) + "\n"
        path_str += "Edges:"
        node_count = 0
        for index in range(len(vertices)):
            if self.parents[index] is not None:
                if node_count % 5 == 0:
                    path_str += "\n"
                path_str += ("(" + vertices[self.parents[index]] + ", "
                                 + vertices[index] + ")")
                node_count += 1
        path_str += "\n"

        return path_str
