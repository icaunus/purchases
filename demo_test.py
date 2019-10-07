import unittest
import demo

class TestDemo(unittest.TestCase):
  def test_load(self):
    self.assertIsNotNone(demo.load('data/1.json'))

  def test_extract(self):
    self.assertEqual(len(demo.extract()), 2)

if __name__ == '__main__':
  unittest.main()
