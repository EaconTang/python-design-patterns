# coding=utf8
"""
模版方法模式
类似于Java的接口设计，通过抽象类定义算法的基本骨架，由子类实现具体方法。
"""
from abc import ABCMeta, abstractmethod


class IClass(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def foo(self):
        raise NotImplementedError

    def bar(self):
        print 'Bar...'

    def act(self):
        self.foo()
        self.bar()


class FooBar(IClass):
    def foo(self):
        print 'Foo...'


if __name__ == '__main__':
    FooBar().act()
    # 输出：
    # Foo...
    # Bar...
