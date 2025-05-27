from shapes import Point, Line
class Shape():
  def __init__(self, is_regular: bool, edge: list[Line], vertice: list[Point]):
    self.edge = Line(start = Point(0,0), end = Point())
    self.is_regular = is_regular
    self.edge = edge
    self.vertice = vertice

  def vertices(self) -> "Point":
    pass
      
  def edges(self) -> "Line":
    pass
      
  def compute_area(self) -> "float":
    pass
      
  def compute_perimeter(self) -> "float":
    pass
      
  def compute_inner_angels(self) -> "float":
    pass