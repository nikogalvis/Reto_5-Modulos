from shapes import Point

class Line:
  def __init__(self, start: "Point" = Point(0,0), end: "Point" = Point(0,0)):
    self.start = start
    self.end = end
   
  def __repr__(self):
    return f"Start: {self.start}  End: {self.end}"
  
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    linea = Line(start=p1, end=p2)
    print(linea)