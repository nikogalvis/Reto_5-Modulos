from math import acos, degrees
from shapes import Point, Line, Shape
class Triangle(Shape):
  def __init__(self,  point_1 = Point(0,0), point_2 = Point(0,0), point_3 = Point(0,0)):
    super().__init__(is_regular = True, edge = [], vertice = [])
    self.point_1 = point_1
    self.point_2 = point_2
    self.point_3 = point_3

    self.edge_1 = Line(start = self.point_1, end = self.point_2)
    self.edge_2 = Line(start = self.point_2, end = self.point_3)
    self.edge_3 = Line(start = self.point_3, end = self.point_1)

    self.v1 = [self.point_2.x - self.point_1.x, self.point_2.y - self.point_1.y]
    self.v1_inv = [self.point_1.x - self.point_2.x, self.point_1.y - self.point_2.y]
    self.v2 = [self.point_3.x - self.point_2.x, self.point_3.y - self.point_2.y]
    self.v2_inv = [(self.point_2.x - self.point_3.x)*-1, self.point_2.y - self.point_3.y]    
    self.v3 = [self.point_3.x - self.point_1.x, self.point_3.y - self.point_1.y]
    self.v3_inv = [(self.point_1.x - self.point_3.x)*-1, self.point_1.y - self.point_3.y]    
    self.angles = self.compute_inner_angles()
    self.sides_lenght = self.auxiliar_width()

  def vertices(self) -> list[Point]:
    return [self.point_1, self.point_2, self.point_3]
      
  def vertices_repr(self) -> list[Point]:
    list_vertices = ["This are the vertices of the Triangle",
                      f"Point 1: {self.point_1}", 
                      f"Point 2: {self.point_2}",
                      f"Point 3: {self.point_3}"]
    return list_vertices

  def edges_repr(self) -> list[Line]:
    list_edges = ["These are the sides of the Triangle",
                  f"Edge 1: {self.edge_1}", 
                  f"Edge 2: {self.edge_2}",
                  f"Edge 3: {self.edge_3}"]
    return list_edges  

  def auxiliar_width(self) -> list[float]:
    va = [self.point_2.x - self.point_1.x, self.point_2.y - self.point_1.y]
    vb = [self.point_3.x - self.point_2.x, self.point_3.y - self.point_2.y]
    vc = [self.point_3.x - self.point_1.x, self.point_3.y - self.point_1.y]
    hip1 = ((va[0]**2)+(va[1]**2))**0.5
    hip2 = ((vb[0]**2)+(vb[1]**2))**0.5
    hip3 = ((vc[0]**2)+(vc[1]**2))**0.5
    return (hip1, hip2, hip3)
    
  def compute_perimeter(self) -> float:
    s = 0
    for i in self.auxiliar_width():
      s += i
    return s
    
  def compute_perimeter_repr(self) -> list:
    return ["Perimeter of Triangle: "] + [self.compute_perimeter()]
  
  def compute_area(self) -> float:
    s = self.compute_perimeter()/2
    a = self.sides_lenght[0]
    b = self.sides_lenght[1]
    c = self.sides_lenght[2]
    return round((s*(s-a)*(s-b)*(s-c))**0.5, 5)
    
  def compute_area_repr(self) -> list:
    return ["Area of Triangle: "] + [self.compute_area()]
    
  def compute_inner_angles(self) -> list[float]:
    # This is for help to remember the vectors
    # self.v1 = [self.point_2.x - self.point_1.x, self.point_2.y - self.point_1.y]
    # self.v1_inv = [self.point_1.x - self.point_2.x, self.point_1.y - self.point_2.y]
    # self.v2 = [self.point_3.x - self.point_2.x, self.point_3.y - self.point_2.y]
    # self.v3 = [self.point_3.x - self.point_1.x, self.point_3.y - self.point_1.y]

    point_product_1 = self.v1[0]*self.v3[0] + self.v1[1]*self.v3[1]
    point_product_2 = self.v1_inv[0]*self.v2[0] + self.v1_inv[1]*self.v2[1]

    hip_1 = ((self.v1[0]**2)+(self.v1[1]**2))**0.5
    hip_2 = ((self.v2[0]**2)+(self.v2[1]**2))**0.5
    hip_3 = ((self.v3[0]**2)+(self.v3[1]**2))**0.5        

    degree_1 = point_product_1/(hip_1*hip_3)
    degree_2 = point_product_2/(hip_1*hip_2)

    angle_1 = round(degrees(acos(degree_1)), 1)
    angle_2 = round(degrees(acos(degree_2)), 1)
    angle_3 = round(180 -(angle_1 + angle_2), 1)
    return [angle_1,angle_2,angle_3]

  def inner_angles(self) -> list[float]:
    return ["Inner Angles of Triangle"] + self.angles

  def __repr__(self) -> str:
    repr = (self.vertices_repr() + self.edges_repr() + self.inner_angles() 
            + self.compute_area_repr() + self.compute_perimeter_repr())
    for i in repr:
      print(i)
    return "That is all i got"