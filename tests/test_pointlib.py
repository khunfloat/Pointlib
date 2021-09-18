from Pointlib.pointlib import *

def test1():
    point = Point(2, 3)
    assert point.x == 2

def test2():
    point = Point(2, 3)
    assert point.y == 3.0

def test3():
    point = Point(2, 3, 1)
    assert point.z == 1.0

def test4():
    point = Point(2, 3)
    assert point.coor == (2.0, 3.0, 0.0)

def test5():
    point = Point(2, 3)
    assert point.get_x() == 2.0

def test6():
    point = Point(2, 3)
    assert point.get_y() == 3.0

def test7():
    point = Point(2, 3, 1)
    assert point.get_z() == 1.0

def test8():
    point = Point(2, 3, 1)
    assert point.neg_x() == -2.0

def test9():
    point = Point(2, 3, 1)
    assert point.neg_y() == -3.0

def test10():
    point = Point(2, 3, 1)
    assert point.neg_z() == -1.0

def test11():
    point = Point(1, 0)
    assert point.slope_from_origin() == 0.0

def test12():
    point1 = Point(1, 0)
    point2 = Point(2, 0)
    assert distance(point1, point2) == 1.0

def test13():
    point1 = Point(0, 0)
    point2 = Point(1, 0)
    assert slove2D(point1, point2) == 0.0

def test14():
    point1 = Point(1, 0)
    point2 = Point(3, 0)
    assert halfway2D(point1, point2).to2D() == (2.0, 0.0)

def test15():
    point1 = Point(1, 0)
    point2 = Point(3, 0)
    assert halfway2D(point1, point2).to3D() == (2.0, 0.0, 0.0)


