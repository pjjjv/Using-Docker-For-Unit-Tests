import unittest
import program

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(program.main1(1, 2), 3)

    def test2(self):
        self.assertEqual(program.main1(3, 2), 5)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
