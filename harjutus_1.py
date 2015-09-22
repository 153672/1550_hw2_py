__author__ = 'Mart Aarma'

import geom
import math

p1 = geom.Point(10.0, 20.0)
p2 = geom.Point(17.0, 0.0)
print("Distants p1 ja p2 vahel: %f" % p1.distance(p2));

p3 = geom.Point(15.0, 17.0)
p3.rotate(geom.Point(0.0,0.0), math.pi/3)
print("Punkti asukoht peale keerutamist: ")
print(p3)