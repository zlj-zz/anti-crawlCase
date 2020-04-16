import requests
from loguru import logger
from retrying import retry


class BaseSpider:
    """crawler's base class"""
    urls = []

    def fetch(self, url, **kwargs):
        """get web page source code

        :url: TODO
        :**kwargs: TODO
        :returns: TODO

        """
        @retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None)
        try:
            response = requests.get(url, **kwargs)
            if response.status_code == 200:
                return response.text
        except requests.ConnectionError:
            return

        @logger.catch
        def crawl(self):
            """crawl main method

            :f: TODO
            :returns: TODO

            """
            for url in self.urls:
                logger.info('fetch {url}'.format(url=url))
                html = self.fetch(url)
                for proxy in self.parse(html):
                    logger.info('fetch proxy {proxy_str} from {url}'.format(
                        proxy_str=proxy, url=url))
                    yield proxy
