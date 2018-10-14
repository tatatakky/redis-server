# -*- coding:utf-8 -*-
def main(key):
    import redis
    from connection_redis import cnct_rds
    from delete_redis import deleter
    from judge_redis import exists_key
    r = cnct_rds()
    #exits_key関数(↓)でkey値が既存の場合、そのvalueが返り値となる。
    value = exists_key(r, key)
    #setter(r) #テスト用にセット
    #deleter(r) #あるkey、valueが不要になったらそのkeyをdelete
    return value

if __name__ == '__main__':
    import sys
    value = main(sys.argv[1])
    print(value)
