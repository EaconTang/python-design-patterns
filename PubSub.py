# coding=utf8
"""
“发布－订阅模式”一般用于解耦消息的发送和接收。发布者无需关心接受对象，只需把消息发送到一个中间代理中间代理(Broker)；订阅者可以根据主题来订阅感兴趣的消息，由Broker来路由消息的去向。
"""


class Broker(object):
    """
    Broker中间代理
    """
    def __init__(self, name=''):
        self._name = name
        self._subscribers = []      # 维护一个订阅者列表

    def attach(self, subscriber):
        """绑定一个订阅者"""
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def detach(self, subscriber):
        """解绑"""
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def route(self, msg, topic=''):
        """路由消息的方法"""
        for subscriber in self._subscribers:
            if topic in subscriber.topic:
                subscriber.sub(msg)


class Publisher(object):
    """发布者"""
    def __init__(self, name, broker):
        self._name = name
        self._broker = broker

    def pub(self, msg, topic=''):
        print '[Publisher: {}] topic: {}, message: {}'.format(self._name, topic, msg)
        self._broker.route(msg, topic)


class Subscriber(object):
    """订阅者"""
    def __init__(self, name, broker, topic=None):
        self._name = name
        broker.attach(self)
        self._topic = [] if topic is None else topic

    def sub(self, msg):
        print '[Subscriber: {}] got message: {}'.format(self._name, msg)

    @property
    def topic(self):
        return self._topic


def main():
    # 声明一个中间代理
    broker = Broker()

    # 声明两个发布者p1、p2，连接到指定的broker
    p1 = Publisher('p1', broker)
    p2 = Publisher('p2', broker)

    # 声明两个订阅者s1、s2，连接到指定的broker，订阅指定的topic
    s1 = Subscriber('s1', broker, topic=['A'])
    s2 = Subscriber('s2', broker, topic=['A', 'B'])

    # p1、p2发布消息
    p1.pub('hello s1', topic='A')
    p2.pub('hello s2', topic='B')


if __name__ == '__main__':
    main()

    # 输出结果：
    # [Publisher: p1] topic: A, message: hello s1
    # [Subscriber: s1] got message: hello s1
    # [Subscriber: s2] got message: hello s1
    # [Publisher: p2] topic: B, message: hello s2
    # [Subscriber: s2] got message: hello s2