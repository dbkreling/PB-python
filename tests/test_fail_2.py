#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time


class MyTest4(unittest.TestCase):
    def test_fail_sleep(self):
        time.sleep(1)
        return self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
