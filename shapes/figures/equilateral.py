from shapes import Point, Triangle

class Equilateral(Triangle):
  def __init__(self, width: float, left_point: "Point"):
    self.width = width
    self.left_point = left_point

    height = (((3)**0.5/2)) * width

    point_1 = left_point
    point_2 = Point(left_point.x + width, left_point.y)
    point_3 = Point(left_point.x + width/2, left_point.y + height)

    super().__init__(point_1=point_1, point_2=point_2, point_3=point_3)