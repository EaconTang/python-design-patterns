# coding=utf8
"""
工厂模式
工厂模式应用广泛，简单但十分有内涵，抽象、封装、继承、委托、多态等面向对象设计中的理论都得到了很好的体现。
"""


class ProgrammerInterface(object):
    """开发者的接口定义"""

    def hello_world(self):
        raise NotImplementedError


class Pythoner(ProgrammerInterface):
    """Python开发者实现hello_world方法"""

    def hello_world(self):
        return 'print "Hello World!"'


class Javaer(ProgrammerInterface):
    """Java开发者实现hello_world方法"""

    def hello_world(self):
        return 'System.out.println("Hello World!")'


def get_programmer(language):
    """获取不同语言开发者的工厂方法"""
    return {
        'python': Pythoner(),
        'java': Javaer(),
    }.get(str(language).lower(), None)


def test_simple_factory():
    # 创建一个python开发者，并查看python语言的hello world方法
    pythoner = get_programmer('python')
    print pythoner.hello_world()

    # 创建一个Java开发者，并查看Java语言的hello world方法
    javaer = get_programmer('Java')
    print javaer.hello_world()

    # 输出：
    # print "Hello World!"
    # System.out.println("Hello World!")


if __name__ == '__main__':
    test_simple_factory()
