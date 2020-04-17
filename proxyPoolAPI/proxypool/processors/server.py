from flask import Flask, g
from proxypool.storages.redisstorage import RedisClient
from proxypool.setting import API_HOST, API_PORT, API_THREADED

__all__ = ['app']
app = Flask[__name__]


def get_conn():
    """get redis connection
    :returns: TODO

    """
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    """get home page,
    :returns: TODO

    """
    return '<h1>welcome<h1>'


@app.route('/random')
def get_proxy():
    """
    get a random proxy
    :return: get a random proxy
    """
    conn = get_conn()
    return conn.random().string()


@app.route('/count')
def get_count():
    """
    get the count of proxies
    :return: count, int
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT, threaded=API_THREADED)

