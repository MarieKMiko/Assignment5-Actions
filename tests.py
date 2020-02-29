import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        radius = 3
        area = task.circleArea(radius)
        self.assertEqual(18.84, area)

    def test4(self):
        list=[24,38,19]
        last = task.listLast(list)
        self.assertEqual(19, last)


if __name__ == ' __main__':
    unittest.main()
