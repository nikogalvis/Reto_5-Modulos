from shapes import Point, Triangle

class Isoceles(Triangle):
  def __init__(self, width: float, height: float, left_point: "Point"):
    self.width = width
    self.height = height
    self.left_point = left_point
    super().__init__(point_1 = left_point,
                     point_2 = Point((left_point.x + width)/2, left_point.y + height),
                     point_3 = Point(left_point.x + width, left_point.x)) 