#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class MyTest1(unittest.TestCase):
    def test_fail_0(self):
        var_1 = 1
        var_2 = 2
        return self.assertEquals(var_1, var_2)

def main():
    unittest.main()



if __name__ == '__main__':
    main()
