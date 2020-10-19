import re
from proxypool.schemas import Proxy


def is_valid_proxy(data):
    """is data is valid proxy format

    :data: TODO
    :returns: TODO

    """
    return re.match(r'\d+\.\d+\.\d+\.\d+\:\d+', data)


def convert_proxy_or_proxies(data):
    """conver list of string to valid proxies or proxy

    :data: TODO
    :returns: TODO

    """
    if not data:
        return None
    if isinstance(data, list):
        result = []
        for item in data:
            item = item.strip()
            if not is_valid_proxy(item): continue
            host, port = item.split(':')
            result.append(Proxy(host=host, port=int(port)))
        return result
    if isinstance(data, str) and is_valid_proxy(data):
        host, port = data.split(':')
        return Proxy(host=host, port=port)

