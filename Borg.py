# coding=utf8
"""
Borg模式
与单例模式接近，我们只需确保所有的实例共享属性和方法（即指向同一个instance.__dict__），这样可以同时保持实例id的区别
"""


class FooBorg(object):
    _share = {}

    def __new__(cls, *args, **kwargs):
        """重写构造函数，将实例属性方法指向这个类变量_share"""
        self = object.__new__(cls, *args, **kwargs)
        self.__dict__ = cls._share
        return self

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name


if __name__ == '__main__':
    f1 = FooBorg('bar')
    f2 = FooBorg('bar')

    print id(f1), id(f2)  # 两个实例id不同
    print f1.__dict__  # f1,f2两个实例变量相同
    print f2.__dict__

    f1.name = 'foobar'  # 通过实例f1修改变量
    print f1.__dict__
    print f2.__dict__  # 实例2的变量也被修改

    # 输出：
    # 4429175888 4429175952
    # {'_name': 'bar'}
    # {'_name': 'bar'}
    # {'_name': 'foobar'}
    # {'_name': 'foobar'}
