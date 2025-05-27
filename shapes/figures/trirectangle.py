from shapes import Point, Triangle
class TriRectangle(Triangle):
  def __init__(self, left_point: "Point", width: float, height: float):
    point_1 = left_point
    point_2 = Point(point_1.x + width, point_1.y)
    point_3 = Point(point_1.x, point_1.y + height)
    super().__init__(point_1 = point_1, point_2 = point_2, point_3 = point_3)