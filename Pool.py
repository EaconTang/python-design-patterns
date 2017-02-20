# coding=utf8
"""
对象池模式
对象池是一定数量的预先创建对象的集合，为了节省创建对象的开销，这些对象可以被客户端取走并归还。
"""
from Queue import Queue


class Pool(object):
    """对象池"""

    def __init__(self, backend, block=True, timeout=None):
        assert isinstance(backend, Queue)
        self._queue = backend  # Queue.Queue队列存储对象池的对象
        self._block = block  # 是否异步获取和存放对象
        self._timeout = timeout  # 超时时间
        self._object = None  # 获取的当前对象

    def _get(self, _block=True, _timeout=None):
        self._object = self._queue.get(block=_block, timeout=_timeout)
        return self._object

    def _put(self, _item, _block=True, _timeout=None):
        return self._queue.put(item=_item, block=_block, timeout=_timeout)

    def __enter__(self):
        print 'get an object...'
        return self._get(_block=self._block, _timeout=self._timeout)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'putback an object...\n'
        self._put(_item=self._object, _block=self._block, _timeout=self._timeout)


# from contextlib import contextmanager
# @contextmanager
# def _pool(queue):
#     """
#     Pool对象池类的contextmanager的实现方式
#     """
#     _object = queue.get()
#     try:
#         print "yield an object..."
#         yield _object
#     except:
#         pass
#     finally:
#         print "putback an object..."
#         queue.put(_object)


def test_pool(pool):
    """测试方法：pool需要实现上下文协议"""
    # 创建队列:：['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    size = 10
    q = Queue(maxsize=size)
    for i in range(size):
        q.put(str(i))

    # 测试对象池类Pool
    for i in range(size * 2):
        with pool(q) as obj:
            # 这里已经获取了一个对象
            print 'Object: {}'.format(obj)
            # 退出with语句时自动放回对象


if __name__ == '__main__':
    test_pool(Pool)

    # 输出：
    # get an object...
    # Object: 0
    # putback an object...

    # get an object...
    # Object: 1
    # putback an object...

    # get an object...
    # Object: 2
    # putback an object...

    # get an object...
    # Object: 3
    # putback an object...

    # get an object...
    # Object: 4
    # putback an object...

    # get an object...
    # Object: 5
    # putback an object...

    # get an object...
    # Object: 6
    # putback an object...

    # get an object...
    # Object: 7
    # putback an object...

    # get an object...
    # Object: 8
    # putback an object...

    # get an object...
    # Object: 9
    # putback an object...

    # get an object...
    # Object: 0
    # putback an object...

    # get an object...
    # Object: 1
    # putback an object...

    # get an object...
    # Object: 2
    # putback an object...

    # get an object...
    # Object: 3
    # putback an object...

    # get an object...
    # Object: 4
    # putback an object...

    # get an object...
    # Object: 5
    # putback an object...

    # get an object...
    # Object: 6
    # putback an object...

    # get an object...
    # Object: 7
    # putback an object...

    # get an object...
    # Object: 8
    # putback an object...

    # get an object...
    # Object: 9
    # putback an object...
