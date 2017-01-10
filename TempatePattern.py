# coding=utf8
"""
模版模式
类似于Java的接口设计
"""
from abc import ABCMeta, abstractmethod


class IClass(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def foo(self):
        pass


class Foo(IClass):
    def foo(self):
        pass


if __name__ == '__main__':
    Foo()