# -*- coding:utf-8 -*-
def db_handle(key):
    import redis
    from connection_redis import cnct_rds
    from judge_redis import exists_key
    li = []
    r = cnct_rds()
    value = exists_key(r, key)
    li.append(key) #listにkeyを追加
    li.append(value) #listにvalueを追加

    return li
