def matchtyper(li):
    #処理
    import json
    import collections as cl
    data = cl.OrderedDict()
    data[li[0]] = li[1]
    ys = cl.OrderedDict()
    d = ys[li[0]] = data
    return d
    #もしjsonファイルに書き出す場合。↓の処理
    #fw = open('test.json','w')
    #json.dump(ys,fw,indent=4)

if __name__ == '__main__':
    li = ["Kodai",[165, 60, "male"]]
    result = matchtyper(li)
    print(result)
