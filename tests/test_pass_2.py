#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time


class TestPass2(unittest.TestCase):
    def test_pass_2(self):
        time.sleep(3)
        return 0


if __name__ == '__main__':
    unittest.main()
