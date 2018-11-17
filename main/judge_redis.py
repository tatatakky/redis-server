def exists_key(r, k):
    #key値がある場合はgetter関数が呼ばれる
    from get_redis import getter
    from set_redis import setter
    from flask import Flask, jsonify, abort, make_response
    if r.exists(k) is True:
        return getter(r, k)
    else:
        return None
