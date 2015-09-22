__author__ = 'Mart Aarma'

import geom
import geom2
import math

p1 = geom.Point(0.5, -4.5)
p2 = geom2.Point(0.5, -4.5)

p1.centre_rotate(math.pi/3)
print(p1)

p2.centre_rotate(math.pi/3)
print(p2)