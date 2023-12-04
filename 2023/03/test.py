import unittest
from main import main


class Test202303(unittest.TestCase):
    def test_202303(self):
        result = main("sampleinput.txt")

        self.assertEqual(4361, result[0])
        self.assertEqual(467835, result[1])

    def test_202303_01(self):
        result = main("testinputs/01.txt")

        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])

    def test_202303_02(self):
        result = main("testinputs/02.txt")

        self.assertEqual(21, result[0])
        self.assertEqual(110, result[1])

    def test_202303_03(self):
        result = main("testinputs/03.txt")

        self.assertEqual(20, result[0])
        self.assertEqual(100, result[1])


if __name__ == "__main__":
    unittest.main()
