import Point
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
		self.origin = Point.point(0,0)

		self.a1 = Point.point(-1,1)
		self.b1 = Point.point(-5,5)

		self.a2 = Point.point(1,1)
		self.b2 = Point.point(5,5)
		
		self.a3 = Point.point(1,-1)
		self.b3 = Point.point(5,-5)
		
		self.a4 = Point.point(-1,-1)
		self.b4 = Point.point(-5,-5)
		
		self.c = Point.circle(0,0,50)
		self.c1 = Point.circle(-2,3,10)
		self.c2 = Point.circle(2,3,10)
		self.c3 = Point.circle(2,-3,10)
		self.c4 = Point.circle(-2,-3,10)


    def test_point_distance(self):
        # make sure distance computations proceed as expected

		# dist 0
		self.assertEqual(self.a1.distFrom(self.a1),0)
		self.assertEqual(self.c.distFrom(self.c),0)
		
		# quad 1 internal
		self.assertEqual(self.a1.distFrom(self.b1),32)
		self.assertEqual(self.a1.distFrom(self.b1),self.b1.distFrom(self.a1))
		
		# quad 1 to 2
		self.assertEqual(self.a1.distFrom(self.a2),4)
		self.assertEqual(self.a1.distFrom(self.b2),52)
		self.assertEqual(self.b1.distFrom(self.a2),52)
		self.assertEqual(self.b1.distFrom(self.b2),100)
		
		# quad 1 to 4
		self.assertEqual(self.a1.distFrom(self.a4),4)
		self.assertEqual(self.a1.distFrom(self.b4),52)
		self.assertEqual(self.b1.distFrom(self.a4),52)
		self.assertEqual(self.b1.distFrom(self.b4),100)
  
    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)
    # 
    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()