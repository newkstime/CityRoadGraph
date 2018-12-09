from comparable import Comparable
from vertex import Vertex

class City(Vertex, Comparable):
    """
    This class represents a city on a graph 
    """
    def __init__(self, name, x, y, pop):
        """
	    Create a city for a Graph.
	    The instance variables are:
	        gps_X: float: Longitide
	        gps_Y: float: Latitide
	        pop: int: Population
	        name: str: Pass to Vertex constructor
	    """
        super().__init__(name)
        self.gps_X = x
        self.gps_Y = y
        self.pop = pop

    def get_X(self):
        """
        Return the City longitude
        """
        return self.gps_X

    def get_Y(self):
        """
        Return the City latitude
        """
        return self.gps_Y

    def get_pop(self):
        """
        Return the City poulation
        """
        return self.pop

    def compare(self, other_city):
        """
        Use the City poulations for comparison
        """
        return self.pop - other_city.get_pop()

    def __str__(self):
        """
        Return a string representation for the City
        """
        return "City name: " + self.get_name() + " City population: " + str(self.get_pop()) + " X: " + "{0:.2f}".format(self.get_X()) + " Y: " "{0:.2f}".format(self.get_Y())

