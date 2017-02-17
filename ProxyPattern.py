# coding=utf8
"""代理模式"""


class Proxy(object):
    """实现代理类"""
    def __init__(self, obj):
        self._obj = obj  # 代理的对象

    def __getattr__(self, item):
        """代理模式的本质，由Proxy类传递方法调用"""
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        """通过Proxy类设置代理对象的属性"""
        if key.startswith('_'):
            super(Proxy, self).__setattr__(key, value)
        else:
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        """通过Proxy类删除代理对象的属性"""
        if item.startswith('_'):
            super(Proxy, self).__delattr__(item)
        else:
            delattr(self._obj, item)


class Test(object):
    def __init__(self, name):
        self._name = name

    def foo(self):
        print 'foo ' + str(self._name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name


if __name__ == '__main__':
    # 被代理的对象
    t = Test('bar')
    # 代理
    proxy = Proxy(t)

    # 通过代理访问属性
    print proxy.name
    proxy.foo()

    # 通过代理设置属性
    proxy.name = 'bra'
    print proxy.name
    proxy.foo()


    # 输出
    # bar
    # foo bar
    # bra
    # foo bra
