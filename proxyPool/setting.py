import platform
from os.path import dirname, abspath, join
from loguru import logger
from environs import Env
# form proxyPool.utils.parse import parse_redis_connection_string

env = Env()
env.read_env()

IS_WINDOWS = platform.system().lower() == 'windows'

# definition of dirs
ROOT_DIR = dirname(dirname(abspath(__file__)))
LOG_DIR = join(ROOT_DIR, env.str("LOG_DIR", 'logs'))

# definition of environments
DEV_MODE, TEST_MODE, PROD_MODE = 'dev', 'test', 'prod'
