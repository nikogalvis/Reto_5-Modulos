from shapes import Point, Line, Rectangle, Square, Triangle, Isoceles, Scalene
if __name__ == "__main__":
  data_1 = Line(start = Point(0,0), end = Point(5,5))
  data_2 = Rectangle(left_down = Point(0,0), right_up = Point(4,3))
  data_3 = Square(square_size = 4, left_down = Point(0,0))
  data_4 = Triangle(point_1 = Point(-1,-1), point_2 = Point(-3,-4), point_3 = Point(5,2))
  data_5 = Isoceles(width = 3,  height = 4, left_point = Point(0,0))
  data_6 = Scalene(point_1 = Point(0,0), point_2 = Point(0,-3), point_3 = Point(1,4))
  print(data_6.__repr__())