import unittest
from main import main


class Test202301(unittest.TestCase):
    def test_202301(self):
        self.assertEqual(281, main("sampleinput.txt"))


if __name__ == "__main__":
    unittest.main()
