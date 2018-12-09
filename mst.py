from graphTree import GraphTree
class MST(GraphTree):
    """
    This class presents a tree for storing the MST
    """
    def __init__(self, root, parents, search_order, total_weight):
        """
        Create an MST
        Instance variables: total_weight: int
        """
        super().__init__(root, parents, search_order)
        self.total_weight = total_weight

    def get_total_weight(self):
        """
        Return total weight of MST
        """
        return self.total_weight
