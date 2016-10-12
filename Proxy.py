class Proxy(object):
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        # do not expose private attributes
        if key.startswith('_'):
            super(Proxy, self).__setattr__(key, value)
        else:
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super(Proxy, self).__delattr__(item)
        else:
            delattr(self._obj, item)


class Test(object):
    def __init__(self, n):
        self._n = n

    def foo(self):
        print 'foo' + str(self._n)


if __name__ == '__main__':
    t = Test(2)
    pt = Proxy(t)
    print pt._n
    pt.a = 1
    print pt.a
    pt._b = 3
    print pt._b

    pt.foo()
    print t.a
