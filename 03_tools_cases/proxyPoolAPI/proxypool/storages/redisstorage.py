import redis
import sys
from proxypool.exceptions import PoolEmptyException
from proxypool.schemas.proxy import Proxy
from proxypool.setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY, PROXY_SCORE_MAX, PROXY_SCORE_MIN, PROXY_SCORE_INIT
from random import choice
from typing import List
from loguru import logger
from proxypool.utils.proxy import is_valid_proxy, conver_proxy_or_proxies

REDIS_CLIENT_VERSION = redis.__version__
IS_REDIS_VERSION_2 = REDIS_CLIENT_VERSION.startswith('2.')


class RedisClient(object):
    """redis connection client of proxypool"""
    def __init__(self,
                 host=REDIS_HOST,
                 port=REDIS_PORT,
                 password=REDIS_PASSWORD,
                 **kwargs):
        """init redis client"""
        self.db = redis.StrictRedis(host=host,
                                    port=port,
                                    password=password,
                                    decode_responses=True,
                                    **kwargs)

    def exists(self, proxy: Proxy) -> bool:
        """if proxy exists

        :proxy: TODO
        :returns: TODO

        """
        return not self.db.zscore(REDIS_KEY, proxy.string()) is None

    def add(self, proxy: Proxy, score=PROXY_SCORE_INIT) -> int:
        """add proxy and set init score

        :proxy: TODO
        :score: TODO
        :returns: TODO

        """
        if not is_valid_proxy('{}:{}'.format(proxy.host, proxy.port)):
            logger.info('invalid proxy {proxy}, throw it'.format(proxy=proxy))
            return 0
        if not self.exists(proxy):
            if IS_REDIS_VERSION_2:
                return self.db.zadd(REDIS_KEY, score, proxy.string())
            return self.db.zadd(REDIS_KEY, {proxy.string(): score})

    def random(self) -> Proxy:
        """get random proxy
        :returns: TODO

        """
        # try to get max score proxy
        proxies = self.db.zrangebyscore(REDIS_KEY, PROXY_SCORE_MAX,
                                        PROXY_SCORE_MAX)
        if len(proxies):
            return conver_proxy_or_proxies(choice(proxies))
        # else get proxy by rank
        proxies = self.db.zrevrange(REDIS_KEY, PROXY_SCORE_MIN,
                                    PROXY_SCORE_MAX)
        if len(proxies):
            return conver_proxy_or_proxies(choice(proxies))
        # else raise error
        raise PoolEmptyException

    def decrease(self, proxy: Proxy) -> int:
        """decrease proxy, if samll than PROXY_SCORE_MIN, delete it

        :proxy: TODO
        :returns: TODO

        """
        score = self.db.zscore(REDIS_KEY, proxy.string())
        # if current score greater than PROXY_SCORE_MIN,decrease
        if score and score > PROXY_SCORE_MIN:
            logger.info('{} current score {}, decrease 1'.format(
                proxy.string(), score))
            if IS_REDIS_VERSION_2:
                return self.db.zincrby(REDIS_KEY, proxy.string(), -1)
            return self.db.zincrby(REDIS_KEY, -1, proxy.string())
        # otherwise delete it
        else:
            logger.info('{} current score {}, remove'.format(
                proxy.string(), score))
            return self.db.zrem(REDIS_KEY, proxy.string())

    def max(self, proxy: Proxy) -> int:
        """if valid,set it max

        :proxy: TODO
        :returns: TODO

        """
        logger.info('{} is valid, set to {}'.format(proxy.string(),
                                                    PROXY_SCORE_MAX))
        if IS_REDIS_VERSION_2:
            return self.db.zadd(REDIS_KEY, PROXY_SCORE_MAX, proxy.string())
        return self.db.zadd(REDIS_KEY, {proxy.string(): PROXY_SCORE_MAX})

    def count(self) -> int:
        """get count
        :returns: TODO

        """
        return self.db.zcard(REDIS_KEY)

    def all(self) -> List[Proxy]:
        """get all proxies
        :returns: TODO

        """
        return conver_proxy_or_proxies(
            self.db.zrangebyscore(REDIS_KEY, PROXY_SCORE_MIN, PROXY_SCORE_MAX))

    def batch(self, start, end) -> List[Proxy]:
        """get batch of proxies

        :start: TODO
        :end: TODO
        :returns: TODO

        """
        return conver_proxy_or_proxies(
            self.db.zrevrange(REDIS_KEY, start, end, -1))


if __name__ == '__main__':
    conn = RedisClient()
    result = conn.random()
    print(result)
