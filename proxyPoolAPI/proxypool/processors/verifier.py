import asyncio
import aiohttp
from loguru import logger
from asyncio import TimeoutError
from aiohttp import ClientProxyConnectionError, ServerDisconnectedError, ClientOSError, ClientHttpProxyError

from proxypool.schemas import Proxy
from proxypool.storages.redisstorage import RedisClient
from proxypool.setting import TEST_TIMEOUT, TEST_BATCH, TEST_URL, TEST_VALID_STATUS

EXCEPTIONS = (ClientProxyConnectionError, ConnectionRefusedError, TimeoutError,
              ServerDisconnectedError, ClientOSError, ClientHttpProxyError)


class ProxyVerifier(object):
    """verifying proxies in queue"""
    def __init__(self):
        self.redis = RedisClient()
        self.loop = asyncio.get_event_loop()

    async def verify(self, proxy: Proxy):
        """verify one proxy"""
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(
                ssl=False)) as session:
            try:
                logger.debug('verify {}'.format(proxy.string()))
                async with session.get(TEST_URL,
                                       proxy='http://{}'.format(
                                           proxy.string()),
                                       timeout=TEST_TIMEOUT,
                                       allow_redirects=False) as response:
                    if response.status in TEST_VALID_STATUS:
                        self.redis.max(proxy)
                        logger.debug('proxy {} is valid, set max score'.format(
                            proxy.string()))
                    else:
                        self.redis.decrease(proxy)
                        logger.debug(
                            'proxy {} is invalid, decrease score'.format(
                                proxy.string()))
            except Exception:
                self.redis.decrease(proxy)
                logger.debug('proxy {} is invalid, decrease score'.format(
                    proxy.string()))

    @logger.catch
    def run(self):
        """verify main method
        :returns: TODO

        """
        # event loop of aiohttp
        logger.info('stating verifier ....')
        count = self.redis.count()
        logger.debug('{} proxies to verify'.format(count))
        for i in range(0, count, TEST_BATCH):
            start, end = i, min(i + TEST_BATCH, count)
            logger.debug('verifying proxies from {} to {} indeces'.format(
                start, end))
            proxies = self.redis.batch(start, end)
            tasks = [self.verify(proxy) for proxy in proxies]
            self.loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    verifier = ProxyVerifier()
    verifier.run()
