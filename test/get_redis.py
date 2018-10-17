def getter(r, key):
    #return r.get(key).decode()
    li = [v.decode() for v in r.lrange(key, 0, -1)]
    if len(li) > 0:
        return li
    else:
        return "Not Having the KEY: {}".format(key)
