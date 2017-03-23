#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class MyTest3(unittest.TestCase):
    def test_fail_3(self):
        return self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
