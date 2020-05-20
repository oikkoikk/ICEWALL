import requests

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# data는 dict로 만들면 된다
data = {'param1': 0, 'param2': 1}

with requests.Session() as sess:
    # get 요청을 보낼 때는 params에
    rep_get = sess.get(url, params=data)
    # post 요청을 보낼 때는 data에
    rep_post = sess.post(url, data=data)
