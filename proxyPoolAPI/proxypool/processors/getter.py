from loguru import logger
from proxypool.storages.redisstorage import RedisClient
from proxypool.setting import PROXY_NUMBER_MAX
from proxypool.spiders import __all__ as crawlers_cls


class ProxyPoolGetter(object):
    """create proxypool and get proxy"""
    def __init__(self):
        """init db connection and crawlers list"""
        self.redis = RedisClient()
        self.crawlers_cls = crawlers_cls
        self.crawlers = [crawlers_cls() for crawlers_cls in self.crawlers_cls]

    def is_full(self):
        """proxypool if full
        :returns: TODO

        """
        return self.redis.count() >= PROXY_NUMBER_MAX

    @logger.catch
    def run(self):
        """run crawler to get proxy
        :returns: TODO

        """
        if self.is_full():
            return
        for crawler in self.crawlers:
            for proxy in crawler.crawl():
                self.redis.add(proxy)


if __name__ == '__main__':
    getter = ProxyPoolGetter()
    getter.run()
