from attr import attrs, attr


@attrs
class Proxy(object):
    """
    proxy schema
    """
    host = attr(type=str, default=None)
    port = attr(type=int, default=None)

    def __str__(self):
        """
        to string, for print
        """
        return '{host}:{port}'.format(host=self.host, port=self.port)

    def string(self):
        """to string"""
        return self.__str__()


if __name__ == '__main__':
    proxy = Proxy(host='8.8.8.8', port=8888)
    print('proxy', proxy)
    print('proxy', proxy.string())
