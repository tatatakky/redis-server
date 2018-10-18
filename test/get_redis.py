def getter(r, key):
    return [v.decode() for v in r.lrange(key, 0, -1)]
