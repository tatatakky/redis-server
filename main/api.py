def jsonifying(li):
    #処理
    import json
    import collections as cl
    data = cl.OrderedDict()
    data["data"] = li[1]
    ys = cl.OrderedDict()
    ys[li[0]] = data
    fw = open('data.json','w')
    json.dump(ys,fw,indent=4)

