def api(li):
    #処理
    import json
    import collections as cl
    data = cl.OrderedDict()
    data["data"] = li[1]
    ys = cl.OrderedDict()
    ys[li[0]] = data
    fw = open('test.json','w')
    json.dump(ys,fw,indent=4)

if __name__ == '__main__':
    li = ["Kodai",[165, 60, "male"]]
    api(li)
