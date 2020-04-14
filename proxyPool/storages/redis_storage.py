import redis
import sys
sys.path.append('../../proxyPool')
# from proxypool.exceptions import PoolEmptyException
# from proxypool.schemas.proxy import Proxy
# from proxypool.setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY, PROXY_SCORE_MAX, PROXY_SCORE_MIN, PROXY_SCORE_INIT

from random import choice
from typing import List
