import unittest
from closest_neighbour import ClosestNeighbour

class TestStringMethods(unittest.TestCase):

    def test_malformed(self):
        self.assertEqual(ClosestNeighbour(["0000", "1000", "0002", "0002111111"]), 0)
        self.assertEqual(ClosestNeighbour(["0000", "1000", "0002", "1"]), 0)
        self.assertEqual(ClosestNeighbour(["0000", "1000", "02", "111"]), 0)


    def test_not_one(self):
        self.assertEqual(ClosestNeighbour(["0000"]), 0)
        self.assertEqual(ClosestNeighbour(["0000","0000","2000"]), 0)

    def test_not_two(self):
        self.assertEqual(ClosestNeighbour(["1000"]), 0)
        self.assertEqual(ClosestNeighbour(["0100","0000","0000","0000"]), 0)


    def test_ok(self):
        self.assertEqual(ClosestNeighbour(["1002"]),1)
        self.assertEqual(ClosestNeighbour(["1020"]),2)
        self.assertEqual(ClosestNeighbour(["0000", "1000", "0002", "0002"]),2)
        self.assertEqual(ClosestNeighbour(["0000", "1200", "0002", "0002"]),1)
        self.assertEqual(ClosestNeighbour(["0000", "1000", "0000", "0002"]),3)
        self.assertEqual(ClosestNeighbour(["0000001", "0000000", "0000000", "0002000","0000000"]),5)




if __name__ == '__main__':
    unittest.main()