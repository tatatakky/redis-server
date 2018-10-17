def exists_key(r, k):
    #key値がある場合はgetter関数が呼ばれる
    from get_redis import getter
    from set_redis import setter
    val = getter(r, k)
    return val

