# coding=utf8
"""
python风格的Mixin模式，也可叫混入、组合模式
Mixin可以看作多继承的特殊实现，它可以给类混入额外的功能，降低多继承的复杂性（如MRO：旧式类使用深度优先搜索，新式类采用C3算法），并同时具有单继承的单一性和多继承的共有性。
有点儿类似于C语言的预编译、include语法。
"""


class MixinPythoner(object):
    def know_python(self):
        print "I code Python."

    def can_web_develop(self):
        print "Develop web app in Python."

    def hello_world(self):
        print "Hello World in Python."


class MixinJavaer(object):
    def know_java(self):
        print "I code Java."

    def can_web_develop(self):
        print "Develop web app in Java."

    def hello_world(self):
        print "Hello World in Java."


class Programmer(MixinPythoner, MixinJavaer):
    """
    混入两个Mixin类
    如果有Mixin类中有相同的方法，按从左到右的顺序获取优先混入的方法
    如果自己已经有的方法，则不会再混入
    """

    def hello_world(self):
        print "Hello World!"


if __name__ == '__main__':
    p = Programmer()
    p.know_python()
    p.know_java()
    p.can_web_develop()
    p.hello_world()

    # 输出：
    # I code Python.
    # I code Java.
    # Develop web app in Python.
    # Hello World!
