#! /usr/bin/env python
# coding:utf-8

import unittest

from unittest_emo import Dict

"""
单元测试记住点：
1. 单元测试，主要思考测试用例的设计和对应的预期结果（预期结果的设定必须准确，不然测试无意义），测试用例针对的功能结果是否符合。而判断符合与否主要利用unittest模块的断言函数或是自己的判断产生一个断言结果。
2. assertEquel断言用例结果与预期结果是否符合。如果不符合会抛出断言异常。
3. 为什么还要对异常结果也要进行测试？因为异常也是期望的功能结果，所以也要测试，对于异常测试断言使用with self.assertRasies(Error): with代码块中设计异常抛出用例。对于这种测试，只要远离就是捕获预期异常其他直接抛出
4. setUp(self) tearDown(self) 方法分别在每个test开头的方法前和后执行，可以用于产生相同的测试用例环境和删除测试用例环境。
"""

"""
单元测试好处：copy from https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936

单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

"""


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





