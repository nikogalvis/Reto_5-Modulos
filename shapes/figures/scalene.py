from shapes import Point, Triangle
class Scalene(Triangle):
  def __init__(self, point_1: "Point", point_2: "Point", point_3: "Point"):
    super().__init__(point_1 = point_1, point_2 = point_2, point_3 = point_3)
    self.side_1 = round(self.sides_lenght[0], 5)
    self.side_2 = round(self.sides_lenght[1], 5)  
    self.side_3 = round(self.sides_lenght[2], 5)
    
    if (self.side_1 == self.side_2) or (self.side_1 == self.side_3) or (self.side_2 == self.side_3):
      raise ValueError("This is NOT an scalene triangle, try again")