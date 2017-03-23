#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time

class AllTests(unittest.TestCase):
    def test_pass_1(self):
        return 0

    def test_pass_2(self):
        return self.assertTrue(True)

    def test_pass_sleep(self):
        time.sleep(3)
        return 0

    def test_fail_1(self):
        var_1 = "one"
        var_2 = 20
        return self.assertEqual(var_1, var_2)

    def test_fail_3(self):
        return self.assertTrue(False)

    def test_fail_sleep(self):
        time.sleep(1)
        return self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
