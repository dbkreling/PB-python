#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time


class MyTest5(unittest.TestCase):
    def test_pass_sleep(self):
        time.sleep(3)
        return 0


if __name__ == '__main__':
    unittest.main()
