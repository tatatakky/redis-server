def exists_key(r, k):
    #key値がある場合はgetter関数が呼ばれる
    from get_redis import getter
    from set_redis import setter
    truth = r.exists(k)
    if truth is True:
        val = getter(r, k)
        return val
    else:
        pass
        #setter(r, k)
