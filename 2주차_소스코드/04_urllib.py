from urllib.request import urlopen, HTTPError

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

try:
    # url으로 http request를 보낸다
    with urlopen(url) as rep:
        # response로 온 html을 100글자 읽어서 출력한다
        print(rep.read(100))
except HTTPError as e:
    print(e)
else:
    print("end")
