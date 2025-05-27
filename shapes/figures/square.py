from shapes import Point, Line, Shape, Rectangle

class Square(Rectangle):
  def __init__(self, square_size: float, left_down: "Point"):
    self.size = square_size
    self.left_down = left_down
    self.right_up = Point(self.left_down.x + self.size, self.left_down.y + self.size)
    self.right_down = Point(self.right_up.x,self.left_down.y)
    super().__init__(left_down, self.right_up)

  def vertices_repr(self) -> list[Point]:
    list_vertices = ["These are the vertices of the square",
                      f"Left Up: {self.left_up}", 
                      f"Left Down: {self.left_down}",
                      f"Right Down: {self.right_down}", 
                      f"Right Up: {self.right_up}"]
    return list_vertices

  def edges_repr(self) -> list[Line]:
    list_edges = ["These are the sides of the square",
                  f"Left Side: {self.left_side}", 
                  f"Top Side: {self.up_side}",
                  f"Right Side: {self.right_side}", 
                  f"Bottom Side: {self.down_side}"]
    return list_edges

  def inner_angels(self) -> list[float]:
    s = []
    for i in range(len(self.edges())):
      s.append(self.compute_inner_angels())
    return ["Square Angles: "] + s
    
  def compute_area(self) -> float:
    return self.width**2

  def compute_perimeter(self) -> float:
    return 4*self.width