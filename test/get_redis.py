def getter(r, key):
    #return r.get(key).decode()
    li = r.lrange(key, 0, -1)
    return [i.decode() for i in li]

