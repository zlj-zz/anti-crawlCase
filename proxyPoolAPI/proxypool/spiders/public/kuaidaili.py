import re
from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.spiders.base import BaseSpider

BASE_URL = 'https://www.kuaidaili.com/free/inha/{page}/'


class KuaidailiSpider(BaseSpider):
    """
    kuaidaili crawler, https://www.kuaidaili.com/
    """
    urls = [BASE_URL.format(page=page) for page in range(1, 200)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        for item in doc('table tr').items():
            td_ip = item.find('td[data-title="IP"]').text()
            td_port = item.find('td[data-title="PORT"]').text()
            if td_ip and td_port:
                yield Proxy(host=td_ip, port=td_port)
