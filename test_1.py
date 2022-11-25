#!/usr/bin/python3
import unittest

from test_p1 import getSum

class test(unittest.TestCase):
  def test_list_int(self):
    """
    Test case 1
    """
    data = []
    for  i in range(10):
      data.append(i)
    ans = getSum(data)
    self.assertEqual(ans, 35)
    
if _name_ == '_main_':
  unittest.main()
