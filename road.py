import math
from edge import Edge
from comparable import Comparable
"""
Background to Find Direction of Travel:

If you are traveling:

Due East:  you are moving in the positive x direction
Due North: you are moving in the positive y direction
Due West:  you are moving in the negative x direction
Due South: you are moving in the negative y direction

From any point in a plane one can travel 360 degrees.
The 360 degrees can be divided into 4 quadrants of 90 degrees each.
The angles run from 0-90 degrees in a counter-clockwise direction
through each of the four quadrants defined below:
                                            
  a) East to North: called Quadrant I
  b) North to West: called Quadrant II
  c) West to South: called Quadrant III
  d) South to East: called Quadrant IV

To find the direction of travel, you need to find an angle
between the line from P1 to P2 and either

  a) a line parallel to the x-axis OR
  b) a line parallel to the y-axis

The best way to visualize and compute the angle is to transform the 
points (x1, y1) to (x1', y1') and (x2, y2) to (x2',y2') such that 
(x1',y1') is (0,0) and (x2',y2') is in the same relative 
position and distance from (0,0), as (x2,y2) is from (x1,y1).

This transformation is acheived by determining the values of 
a and b from the equation below:

x1': x1 + a = x1' = 0 --> a = -x1
y1': y1 + b = y1' = 0 --> b = -y1

And then adding a and b to x2 and y2:

x2': x2 + -x1 = x2'
y2': y2 + -y1 = y2' 

Using these transformed points, the parallel lines are directly 
on the axes:
  a) Quadrant I:   positive x-axis
  b) Quadrant II:  positive y-axis
  c) Quadrant III: negative x-axis
  d) Quadrant IV:  negative y-axis

In order to find angles, you need to use the Law of Cosines.
The Law of Cosines is used to find the angles of a triangle 
given that you know the length of each side.

The length of sides of right triangles are easy to compute.
We can form right triangles using the line between P1 to P2 as 
the hypotenuse of a right triangle.

The other two sides of the right triangle are either on the 
x-axis and y-axis or parallel to them.

We must define a point P3 that forms the right triangle with 
points P1 and P2 - to find the point P3 = (x3, y3):

Draw the line from P2 which is perpendicular to the line described 
above, depending on the quadrant in which the line of P1 to P2 lies
The coordinates of this point P3 are 
Quadrant I  and Quadrant III: x3 = x2', y3 = y1' = 0
Quadrant II and Quadrant IV:  x3 = x1' = 0, y3 = y2'

To use the Law of Cosines to find the angle, you need the lengths
of all three sides of the right triangle formed with P1, P2, and P3;

You can label the sides and vertices of the right triangle as follows:
  a) side a is across from angle A, whose angle we need to compute
  b) side b is across from angle B
  c) side c is across from angle C, line from P1 to P2 (hypotenuse)

To compute the distance, use the distance formula
  length side c = SQRT [(x2'-x1')**2 + (y2'-y1')**2]
  length side c = SQRT [(x2'-0)**2 + (y2'-0)**2]
  length side c = SQRT [(x2')**2 + (y2')**2]
  
  length side b = SQRT [(x3-x1')**2 + (y3-y1')**2]
  length side b = SQRT [(x3-0)**2 + (y3-0)**2]
  length side b = SQRT [(x3)**2 + (y3)**2]
  
  length side a = SQRT [(x3-x2')**2 + (y3-y2')**2]
  
Law of Cosines:
  angle A = ARCCOS [((b*b) + (c*c) - (a*a)) / 2*b*c]
  where a is length side a, b is length side b, and c is length side c
  
To determine the direction you need to know the quadrant and the angle.
To determine the quadrant, you need to know the relative 
positions between x1' and x2' and between y1' and y2'
  a) Quadrant I:  (x1' <= x2' & y1' <  y2') --> (0 <= x2' & 0 < y2')
  b) Quadrant II: (x1' >  x2' & y1' <= y2') --> (0 >  x2' & 0 <= y2')
  c) Quadrant III:(x1' >= x2' & y1' >  y2') --> (0 >= x2' & 0 >  y2')
  d) Quadrant IV: (x1' >  x2' & y1' >= y2') --> (0 >  x2' & 0 >= y2')
  
We can further divide up the 360 degrees into 16 directions 
of travel, where each direction occupies 22.5 degrees

The possible directions of travel are
  Quadrant I:   E, ENE, NE, NNE, N
  Quadrant II:  N, NNW, NW, WNW, W
  Quadrant III: W, WSW, SW, SSW, S
  Quadrant IV;  S, SSE, SE, ESE. E

The angle slices in these quadrants correspond to traveling in 
one of 16 directions:

Quadrant I (1):   (0.00, 11.25)  : 'E' 
                  (11.25, 33.75) : 'ENE' 
                  (33.75, 56.25) : 'NE'
                  (56.25, 78.75) : 'NNE' 
                  (78.75, 90.0)  : 'N' 
Quadrant II (2):  (0.00, 11.25)  : 'N', 
                  (11.25, 33.75) : 'NNW' 
                  (33.75, 56.25) : 'NW'
                  (56.25, 78.75) : 'WNW'
                  (78.75, 90.0)  : 'W' 
Quadrant III (3): (0.00, 11.25)  : 'W' 
                  (11.25, 33.75) : 'WSW' 
                  (33.75, 56.25) : 'SW'
                  (56.25, 78.75) : 'SSW' 
                  (78.75, 90.0)  : 'S' 
Quadrant IV (4):  (0.00, 11.25)  : 'S'
                  (11.25, 33.75) : 'SSE'
                  (33.75, 56.25) : 'SE'
                  (56.25, 78.75) : 'ESE'
                  (78.75, 90.0)  : 'E' 
"""
class Road(Edge, Comparable):
    """
    This class represents a Road on a map (Graph) 
    """
    def __init__(self, from_city, to_city):
        """
        Creates a new Road
        Instance variables:
            self.direction: str
        """
        super().__init__(from_city, to_city)
        direction, distance = self.comp_direction()
        self.direction = direction
        self.set_weight(distance)

    def get_distance(self):
        """
        Return distance (weight)
        """
        return self.get_weight()

    def compare(self, other_road):
        """
        Use the Road weight (distance) for comparison
        """
        return self.dist - other_road.get_distance()

    def get_direction(self):
        """
        Return direction
        """
        return self.direction()

    def comp_direction(self):
        """
        Compute and return the direction of the Road
        and the distance between the City vertices
        Note: Do NOT round any values (especially GPS) in this method,
	      we want them to have their max precision.
              Only do rounding when displaying values
        """
        # Get the points from the GPS coordinates of each City
        # These are in degrees, change to radians
        x1 = self.from_vertex.get_X()
        y1 = self.from_vertex.get_Y()
        x2 = self.to_vertex.get_X()
        y2 = self.to_vertex.get_Y()
        # Transform the points such that P1 lies at (0,0)
        x1_rad, y1_rad, x2_rad, y2_rad = self.transform_points(x1, y1, x2, y2)
        x1_rad, y1_rad, x2_rad, y2_rad = math.radians(x1_rad), math.radians(y1_rad), math.radians(x2_rad), math.radians(y2_rad)
        # Given the x and y coordinates of P1 and P2,
        # find the quadrant in which the angle exists
        quadrant = self.find_quadrant(x1, y1, x2, y2)
        # Find P3: x and y coordinates
        # Using if / else shorthand
        if quadrant == 1 or quadrant == 3:
            x3_rad = x2_rad
            y3_rad = y1_rad
        else:
            x3_rad = x1_rad
            y3_rad = y2_rad
        # Determine lengths of side a, b, and c
        side_a = self.distance(x2_rad, y2_rad, x3_rad, y3_rad)
        side_b = self.distance(x1_rad, y1_rad, x3_rad, y3_rad)
        side_c = self.distance(x1_rad, y1_rad, x2_rad, y2_rad)

        angle = self.compute_angle(side_a, side_b, side_c)
        direction = self.compute_direction(angle, quadrant)

        side_c_miles = side_c * 3959

        return direction, side_c_miles

    def transform_points(self, x1, y1, x2, y2):
        """
        x1' = 0
        y1' = 0
        x2' = x2 + -x1
        y2' = y2 + -y1
        """
        return 0, 0, x2 - x1, y2 - y1

    def find_quadrant(self, x1, y1, x2, y2):
        """
          a) Quadrant I:   when x2' > 0  and y2' >= 0
          b) Quadrant II:  when x2' <= 0 and y2' > 0
          c) Quadrant III: when x2' < 0  and y2' <= 0
        """
        if x2 > x1 and y2 >= y1:
            return 1
        elif x2 <= x1 and y2 > y1:
            return 2
        elif x2 < x1 and y2 <= y1:
            return 3
        elif x2 >= x1 and y2 < y1:
            return 4

    def distance(self, x1, y1, x2, y2):
        """
        Use distance formula to find length of line from P1 to P2
        """
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def compute_angle(self, side_a, side_b, side_c):
        """
        Use the Law of Cosines to find the angle
        Convert radians to degrees
        """
        return math.degrees(math.acos((side_b**2 + side_c**2 - side_a**2)
                        / (2 * (side_b) * (side_c))))

    def compute_direction(self, angle, quadrant):
        """
        Create a dictionary for each quadrant that holds the angle slices
        for each direction.  The key is a 2-tuple holding the degrees
        (low, high) of the angle slices, and the value is the direction
        """
        q1_dict = {(00.00, 11.25) : 'E', (11.26, 33.75) : 'ENE', (33.76, 56.25) : 'NE',
                   (56.26, 78.75) : 'NNE', (78.76, 90.00) : 'N'}
        q2_dict = {(00.00, 11.25) : 'N', (11.26, 33.75) : 'NNW', (33.76, 56.25) : 'NW',
                   (56.26, 78.75) : 'WNW', (78.76, 90.00) : 'W'}
        q3_dict = {(00.00, 11.25) : 'W', (11.26, 33.75) : 'WSW', (33.76, 56.25) : 'SW',
                   (56.26, 78.75) : 'SSW', (78.76, 90.00) : 'S'}
        q4_dict = {(00.00, 11.25) : 'S', (11.26, 33.75) : 'SSE', (33.76, 56.25) : 'SE',
                   (56.26, 78.75) : 'ESE', (78.76, 90.00) : 'E'}
        if quadrant == 1:
            for degrees, direction in q1_dict.items():
                if angle >= degrees[0] and angle <= degrees[1]:
                    return q1_dict[degrees]
        elif quadrant == 2:
            for degrees, direction in q2_dict.items():
                if angle >= degrees[0] and angle <= degrees[1]:
                    return q2_dict[degrees]
        elif quadrant == 3:
            for degrees, direction in q3_dict.items():
                if angle >= degrees[0] and angle <= degrees[1]:
                    return q3_dict[degrees]
        elif quadrant == 4:
            for degrees, direction in q4_dict.items():
                if angle >= degrees[0] and angle <= degrees[1]:
                    return q4_dict[degrees]

    def __str__(self):
        """
        Return road information as a string
        """
        return self.from_vertex.get_name() + " to " + self.to_vertex.get_name() + " traveling " + self.direction + " for " + "{0:.2f}".format(self.get_distance()) + " miles."
