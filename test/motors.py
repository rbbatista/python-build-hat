import unittest
import time
from buildhat import Motor

class TestMotorMethods(unittest.TestCase):

    def test_rotations(self):
        m = Motor('A')
        pos1 = m.get_position()
        m.run_for_rotations(2) 
        pos2 = m.get_position()
        rotated = (pos2 - pos1)/360
        self.assertLess(abs(rotated - 2), 0.5)

    def test_position(self):
        m = Motor('A')
        m.run_to_position(0)
        pos1 = m.get_aposition()
        diff = abs((0-pos1+180) % 360 - 180)
        self.assertLess(diff, 10)

        m.run_to_position(180)
        pos1 = m.get_aposition()
        diff = abs((180-pos1+180) % 360 - 180)
        self.assertLess(diff, 10)

    def test_time(self):
        m = Motor('A')
        t1 = time.time()
        m.run_for_seconds(5)
        t2 = time.time()
        self.assertEqual(int(t2 - t1), 5)

if __name__ == '__main__':
    unittest.main()