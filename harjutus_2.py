__author__ = 'Mart Aarma'

import geom
import geom2
import math
import unittest

class PointTests(unittest.TestCase) :

    def createPoint(self, x, y):
        return geom.Point(x,y);

    def setUp(self):
        self.p1 = self.createPoint(0.5, -4.5)
        self.p2 = self.createPoint(0.5, 0)

    def testXY(self):
        self.assertAlmostEquals(self.p1.x(), 0.5)
        self.assertAlmostEquals(self.p1.y(), -4.5)
        self.assertAlmostEquals(self.p2.x(), 0.5)
        self.assertAlmostEquals(self.p2.y(), 0)

    def testRho(self):
        self.assertAlmostEquals(self.p1.rho(), math.sqrt(0.5**2 + 4.5**2))

    def testTheta(self):
        self.assertAlmostEquals(self.p1.theta(), math.atan2(-4.5, 0.5))

    def testDistance(self):
        self.assertAlmostEquals(4.5, self.p1.distance(self.p2));
        self.assertAlmostEquals(4.5, self.p2.distance(self.p1));

    def testVectorTo(self):
        v = self.p1.vectorTo(self.p2);
        self.assertAlmostEquals(v.x(), 0)
        self.assertAlmostEquals(v.y(), 4.5)

    def testTranslate(self):
        self.p1.translate(-0.5, 4.5);
        self.assertAlmostEquals(self.p1.x(), 0)
        self.assertAlmostEquals(self.p1.y(), 0)
        self.p1.translate(0.5, -4.5);

    def testScale(self):
        self.p1.scale(10);
        self.assertAlmostEquals(self.p1.x(), 5)
        self.assertAlmostEquals(self.p1.y(), -45)
        self.p1.scale(0.1);

    def testCenterRotate(self):
        self.p1.centre_rotate(math.pi/3);
        self.assertAlmostEquals(self.p1.x(), 4.147114317029974)
        self.assertAlmostEquals(self.p1.y(), -1.816987298107781)
        self.assertAlmostEquals(self.p1.rho(), 4.527692569068709)
        self.assertAlmostEquals(self.p1.theta(), -0.4129415544244033)
        self.setUp()

    def testRotate(self):
        self.p1.rotate(self.p2, math.pi/3);
        self.assertEquals(self.p1.x(), 4.397114317029974)
        self.assertEquals(self.p1.y(), -2.25)
        self.assertEquals(self.p1.rho(), 4.939343510733989)
        self.assertEquals(self.p1.theta(), -0.47296312665809603)
        self.setUp()

class PolarPointTests(PointTests) :

    def createPoint(self, x, y):
        return geom2.Point(x,y);