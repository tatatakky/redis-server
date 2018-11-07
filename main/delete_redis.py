def deleter(r):
    for i in range(10):
        r.delete("name" + str(i))
