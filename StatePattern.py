# coding=utf-8
"""
状态模式
对象在不同的状态下，拥有不同的行为；每个状态封装为一个类，实现自己状态下所具有的方法
"""


class PythonerState(object):
    """python开发经验的状态类"""

    def know_python(self):
        """了解python"""
        raise NotImplementedError()

    def use_metaclass(self):
        """熟悉python"""
        raise NotImplementedError()

    def master_all(self):
        """精通python"""
        raise NotImplementedError()


class JuniorPythoner(PythonerState):
    """初级python开发"""

    def know_python(self):
        return 'Yeah, I konw "hello world".'

    def __str__(self):
        return "初级Pythoner"


class SeniorPythoner(JuniorPythoner):
    """中高级python开发"""

    def use_metaclass(self):
        return "hehh, I know how to use metaclass..."

    def __str__(self):
        return "中高级Pyhoner"


class MasterPythoner(SeniorPythoner):
    """大师级pythoner"""

    def master_all(self):
        return "I konw all internal mechanism."

    def __str__(self):
        return "大师级Pyhoner"


class Pythoner(object):
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, _state):
        self._state = _state

    def __getattr__(self, item):
        return getattr(self._state, item)


def test_pythoner(pythoner):
    print pythoner.state

    try:
        print pythoner.know_python()
    except NotImplementedError:
        print "Sorry, I don't konw python!"
        return

    try:
        print pythoner.use_metaclass()
    except NotImplementedError:
        print "Ahhh, I can't use metacalss!"
        return

    try:
        print pythoner.master_all()
    except NotImplementedError:
        print "Honestly speaking, I still have a lot to learn!"
        return


if __name__ == '__main__':
    pyer = Pythoner(JuniorPythoner())

    test_pythoner(pyer)
    # 输出：
    # 初级Pythoner
    # Yeah, I konw "hello world".
    # Ahhh, I can't use metacalss!

    pyer.state = SeniorPythoner()
    test_pythoner(pyer)
    # 输出：
    # 中高级Pyhoner
    # Yeah, I konw "hello world".
    # hehh, I know how to use metaclass...
    # Honestly speaking, I still have a lot to learn!

    pyer.state = MasterPythoner()
    test_pythoner(pyer)
    # 输出：
    # 大师级Pyhoner
    # Yeah, I konw "hello world".
    # hehh, I know how to use metaclass...
    # I konw all internal mechanism.
