import unittest
from data_transforms.angle_metric import angle_distance


class TestAngleMetric(unittest.TestCase):
    def test_small_angle(self):
        '''Test distance between small angles'''
        a = 10
        b = 90
        expected = 80
        result = angle_distance(a, b)
        self.assertEqual(result, expected)

    # def test_large_angles(self):
    #     '''Test distance between large angles'''
    #     a = 0
    #     b = 270
    #     expected = 90
    #     result = angle_distance(a, b)
    #     self.assertEqual(result, expected)

    # def test_wrapping_angles(self):
    #     '''Test distance around wrapping angle'''
    #     a = 1
    #     b = 359
    #     expected = 2
    #     result = angle_distance(a, b)
    #     self.assertEqual(result, expected)

    # def test_large_input_angles(self):
    #     '''Test distance when input angles are above 360'''
    #     a = 720
    #     b = 270
    #     expected = 90
    #     result = angle_distance(a, b)
    #     self.assertEqual(result, expected)
