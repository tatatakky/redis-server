def cnct_rds():
    import redis
    #接続速度を上げるためにプールを使う。
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)
    return r

