#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class MyTest1(unittest.TestCase):
    def test_fail_1(self):
        var_1 = 1
        var_2 = 2
        return self.assertTrue(var_1, var_2)


if __name__ == '__main__':
    unittest.main()
