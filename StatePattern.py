# coding=utf-8
"""
状态模式
"""


class ConnectionState(object):
    """Connection state base class"""
    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    def read(self):
        raise NotImplementedError()


class ConnectionClosed(ConnectionState):
    def open(self):
        print('open connection...')

    def close(self):
        raise RuntimeError('Connection not open!')

    def read(self):
        raise RuntimeError('Connection not open!')

    def __repr__(self):
        return 'Closed connection'


class ConnectionOpened(ConnectionState):
    def open(self):
        raise RuntimeError('Connection already open!')

    def close(self):
        print('close connection...')

    def read(self):
        print('read connection...')

    def __repr__(self):
        return 'Opened connection'


class Connection(object):
    def __init__(self, state):
        # assert isinstance(state, ConnectionState)
        self._state = state

    def open(self):
        return self._state.open()

    def close(self):
        return self._state.close()

    def read(self):
        return self._state.read()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state

    def __repr__(self):
        return self._state.__repr__()


if __name__ == '__main__':
    opened = Connection(ConnectionOpened())
    print opened
    opened.read()
    opened.close()
    opened.open()

    closed = Connection(ConnectionClosed())
    print closed
    closed.close()
    closed.read()
    closed.open()


