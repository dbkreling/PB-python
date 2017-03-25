#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time


class TestFail2(unittest.TestCase):
    def test_fail_2(self):
        time.sleep(2)
        return self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
