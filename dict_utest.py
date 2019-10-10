#! /usr/bin/env python
# coding:utf-8

import unittest

from unittest_emo import Dict




# 单元测试Dict类

class UnittestDict(unittest.TestCase):

    def test_dict(self):
        d = Dict(a=1, b=2)
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 2)

    def test_key(self):
        d = Dict(a=1, b=2)
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)

    def test_error(self):
        d = Dict(a=1, b=2)
        with self.assertRaises(AttributeError):
            d.empty





