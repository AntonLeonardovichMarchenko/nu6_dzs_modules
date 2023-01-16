import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('go go'.upper(), 'GO GO')

  def test_isupper(self):
      self.assertTrue('GO GO'.isupper())
      self.assertFalse('Go go'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверка того, что s.split НЕ работает,
      # если разделитель - НЕ строка
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
