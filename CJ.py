import unittest
from JAM import stroka

class TestStroka(unittest.TestCase):
    def test_stroka(self):
        self.assertEqual(stroka("privet"), "Privet!")

if __name__ == "__main__":
    unittest.main()