#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestFail1(unittest.TestCase):
    def test_fail_1(self):
        return self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
