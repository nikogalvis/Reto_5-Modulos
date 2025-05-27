from math import acos, degrees
from shapes import Shape, Point, Line

class Rectangle(Shape):
  #* Este __init__ tiene muchos datos, para facilitar el proceso de las demás funciones.
  def __init__(self, left_down: "Point", right_up: "Point"):

    super().__init__(is_regular = True, edge = [], vertice = [])
    self.left_down = left_down
    self.right_up = right_up
    self.left_up = Point(self.left_down.x , self.right_up.y)
    self.right_down = Point(self.right_up.x, self.left_down.y)

    self.left_side = Line(start = self.left_down, end = self.left_up)
    self.up_side = Line(start = self.left_up, end = self.right_up)
    self.right_side = (Line(start = self.right_down,
                       end = self.right_up))
    self.down_side = (Line(start = self.left_down,
                      end = self.right_down))
    
    self.width = (float(self.right_up.x)) - (float(self.left_down.x))
    self.height = (float(self.left_up.y)) - (float(self.right_down.y))
      
  #* Como se puede ver aqui, el __init__ hace mas pasables las formulas
  def vertices(self) -> list[Point]:
    return [self.left_up, self.left_down, self.right_down, self.right_up]
    
  def vertices_repr(self) -> list[Point]:
    list_vertices = ["This are the vertices of the rectangle",
                      f"Left Up: {self.left_up}", 
                      f"Left Down: {self.left_down}",
                      f"Right Down: {self.right_down}", 
                      f"Right Up: {self.right_up}"]
    return list_vertices
    
  def edges(self) -> list[Line]:
    return [self.left_side, self.up_side, self.right_side, self.down_side]
    
  def edges_repr(self) -> list[Line]:
    list_edges = ["This are the sides of the rectangle",
                  f"Left Side: {self.left_side}", 
                  f"Top Side: {self.up_side}",
                  f"Right Side: {self.right_side}", 
                  f"Bottom Side: {self.down_side}"]
    return list_edges
  
  def compute_inner_angels(self) -> float:
    v1 = [self.left_up.x - self.left_down.x, self.left_up.y - self.left_down.y]
    v2 = [self.right_down.x - self.left_down.x, self.right_down.y - self.left_down.y]

    point_product = v1[0]*v2[0] + v1[1]*v2[1]
    hip1 = ((v1[0]**2)+(v1[1]**2))**0.5
    hip2 = ((v2[0]**2)+(v2[1]**2))**0.5

    if (hip1*hip2) == 0: # Uno de los vectores es nulo, no se puede definir ángulo
      return 90
    
    degree = point_product/(hip1*hip2)
    angle = degrees(acos(degree))
    return angle

  def inner_angels(self) -> list[float]:
    s = []

    for i in range(len(self.edges())):
      s.append(self.compute_inner_angels())

    return ["Rectangle Angles: "] + s

  def compute_area_repr(self) -> float:

    if (self.width or self.height) < 0:
      return ["Area: "] + [(self.width*self.height)*(0-1)]
    
    return ["Area: "] + [self.width*self.height]
  
  def compute_area(self) -> float:
    return self.width*self.height
    
  def compute_perimeter_repr(self) -> float:
    return ["Perimeter: "] + [2*(self.width + self.height)]
  
  def compute_perimeter(self) -> float:
    return 2*(self.width + self.height)
    
  def __repr__(self):

    repr = (self.vertices_repr() + self.edges_repr() + self.inner_angels() 
            + self.compute_area_repr() + self.compute_perimeter_repr())
    
    for i in repr:
      print(i)
    return "That is all i got"