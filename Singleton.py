# coding=utf8
"""单例模式"""

from functools import wraps


def singleton(cls):
    _instances = {}  # 容器字典，存储每个类对应生成的实例

    @wraps(cls)
    def wrapper(*args, **kwargs):
        # 检查类是否_instances的key；如果是，直接返回生成过的实例
        key = '<{}_{}_{}>'.format(cls.__name__, args, kwargs)

        if key not in _instances:
            _instances[key] = cls(*args, **kwargs)
        return _instances[key]

    return wrapper


@singleton
class Foo(object):
    def __init__(self, a=0):
        self.a = a


if __name__ == '__main__':
    # 测试
    foo1 = Foo(1)
    foo2 = Foo(1)
    print foo1.a  # Out: 1
    print foo2.a  # Out: 1
    print id(foo1) == id(foo2)  # 结果为True，两个实例id相等，证明这个类确实是单例的

    foo3 = Foo(3)
    print id(foo3) == id(foo1)  # 结果为False，用不同参数初始化的实例，当然也不应该相同
