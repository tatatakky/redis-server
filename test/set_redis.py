#テスト用にdbに値をsetするsetterを用意。
def setter(r):
    for i in range(10):
        r.set("name" + str(i), str(i) + "kun")
