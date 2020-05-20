import requests

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# requests.Session은 쿠키 처리 등을 자동으로 해준다
with requests.Session() as sess:
    # url로 get 요청을 보낸다
    rep = sess.get(url)
    # response에 포함된 html을 출력한다
    print(rep.text)
