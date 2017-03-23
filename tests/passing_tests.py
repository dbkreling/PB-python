#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time

class PassingTests(unittest.TestCase):
    def test_pass_1(self):
        return 0

    def test_pass_2(self):
        return self.assertTrue(True)

    def test_pass_sleep(self):
        time.sleep(3)
        return 0


if __name__ == '__main__':
    unittest.main()
