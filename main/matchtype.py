def matchtyper(li):
    import json
    import collections as cl
    data = cl.OrderedDict()
    data[li[0]] = li[1]
    ys = cl.OrderedDict()
    d = ys[li[0]] = data
    return d
