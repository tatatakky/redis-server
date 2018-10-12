# -*- coding:utf-8 -*-
def setter(r):
    import redis
    for i in range(10):
        r.set("name" + str(i), str(i) + "kun")
    result = r.get("name8")
    print(result)

if __name__ == '__main__':
    from connection_redis import cnct_rds
    redis_server = cnct_rds()
    setter(redis_server)
