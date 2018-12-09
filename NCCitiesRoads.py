from graph import Graph
from road import Road
from city import City
from collections import Counter
"""
For this program:
  1. Create the City and Road lists 
  2. Add 6 City objects to the City (Vertex) list.
  3. Add 18 Road objects to the Road (Edge) list.  
  4. Create a Graph passing in the City and Road lists.
  5. Using the Graph you created: 
     Display each of the items requested below:
        (Look at the Graph methods to do these)
     a. The number of Cities in the map.
     b. The City object information for the 4th City
        added, using a Graph method to retrieve the City.
     c. The City (Vertex) with the largest number of Neighbors
     d. The Road (Edge) information for each Road using a 
        Graph method.
"""
def main():
    """
    The NCCitiesRoads mainline logic creates a graph 
    from city and road information
    """
    # Create a list of City and Road objects
    cities = []
    roads = [0] * 18
    # Create 6 Cities
    murphy = City("Murphy", -84.029924, 35.089848, 1627)
    mars_hill = City("Mars Hill", -82.547843, 35.828496, 1869)
    mooresville = City("Mooresville", -80.820139, 35.584337, 32711)
    morrisville = City("Morrisville", -78.828930, 35.827493, 18576)
    morehead_city = City("Morehead City", -76.746748, 34.727700, 8661)
    manteo = City("Manteo", -75.669385, 35.904595, 1434)
    # Add them to a cities list
    cities.append(murphy)
    cities.append(mars_hill)
    cities.append(mooresville)
    cities.append(morrisville)
    cities.append(morehead_city)
    cities.append(manteo)
    # Create 18 roads and add them to roads list
    roads[0] = Road(murphy, mars_hill)
    roads[1] = Road(murphy, mooresville)
    roads[2] = Road(mars_hill, murphy)
    roads[2].set_weight(1)
    roads[3] = Road(mars_hill, mooresville)
    roads[3].set_weight(1)
    roads[4] = Road(mars_hill, morrisville)
    roads[4].set_weight(1)
    roads[5] = Road(mooresville, murphy)
    roads[5].set_weight(2)
    roads[6] = Road(mooresville, mars_hill)
    roads[6].set_weight(2)
    roads[7] = Road(mooresville, morrisville)
    roads[7].set_weight(2)
    roads[8] = Road(mooresville, morehead_city)
    roads[8].set_weight(2)
    roads[9] = Road(morrisville, mars_hill)
    roads[9].set_weight(2)
    roads[10] = Road(morrisville, mooresville)
    roads[10].set_weight(3)
    roads[11] = Road(morrisville, morehead_city)
    roads[11].set_weight(3)
    roads[12] = Road(morrisville, manteo)
    roads[12].set_weight(3)
    roads[13] = Road(morehead_city, mooresville)
    roads[13].set_weight(4)
    roads[14] = Road(morehead_city, morrisville)
    roads[14].set_weight(4)
    roads[15] = Road(morehead_city, manteo)
    roads[15].set_weight(4)
    roads[16] = Road(manteo, morrisville)
    roads[16].set_weight(5)
    roads[17] = Road(manteo, morehead_city)
    roads[17].set_weight(5)

    # Create weighted Graph map
    graph_map = Graph(cities, roads)
    # Print he number of cities in the map.
    print("The number of cities: " + str(graph_map.get_size()))
    print()
    # Print the City object information for "Morrisville",
    # using a graph method to retrieve the City.
    print(graph_map.get_vertex("Morrisville"))
    print()
    # Determine the City with the largest number 
    # of Roads ending there and print the City name
    most_roads = ""
    road_number = 0
    road_counter = 0
    for city in cities:
        for road in graph_map.neighbors_dict.get(city.get_name()):
            road_counter += 1
        if road_counter > road_number:
            most_roads = city.get_name()
            road_number = road_counter
        road_counter = 0
    print("City with the most roads: " + most_roads)
    print()
    # Print the City and Road edge information using a Graph method.
    # to retrieve the City and Roads
    for city in cities:
        print(city)
        for road in graph_map.neighbors_dict.get(city.get_name()):
            print(road)
        print()

main()
