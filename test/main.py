# -*- coding:utf-8 -*-
def main():
    import sys
    import redis
    from connection_redis import cnct_rds
    from set_redis import setter
    from get_redis import getter
    r = cnct_rds()
    setter(r) #テスト用にセット
    return getter(r, sys.argv[1])

if __name__ == '__main__':
    value = main()
    print(value)
