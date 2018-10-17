def exists_key(r, k):
    #key値がある場合はgetter関数が呼ばれる
    from get_redis import getter
    from set_redis import setter
    try:
        val = getter(r, k)
        return val
    except Exception:
        return "Error : Not having the KEY ({}) in redis-db".format(k)

