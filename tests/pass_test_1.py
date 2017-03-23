#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class MyTest2(unittest.TestCase):
    def test_pass_2(self):
        return self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
