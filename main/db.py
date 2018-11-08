# -*- coding:utf-8 -*-
def db_handle(key):
    import redis
    from connection_redis import cnct_rds
    #from delete_redis import deleter
    from judge_redis import exists_key
    #from jsonconvert import jsonifying
    li = []
    r = cnct_rds()
    #exits_key関数(↓)でkey値が既存の場合、そのvalueが返り値となる。
    value = exists_key(r, key)
    #deleter(r) #あるkey、valueが不要になったらそのkeyをdelete
    li.append(key) #listにkeyを追加
    li.append(value) #listにvalueを追加

    return li

    #jsonifying(li)

if __name__ == '__main__':
    import sys
    db_handle(sys.argv[1])
