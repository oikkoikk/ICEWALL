import requests
import time
import random
from bs4 import BeautifulSoup

pages = ['Python_(programming_language)']


def get_page(sess, page_name):
    # wikipedia의 url에 page_name을 조합해 url을 얻습니다
    url = f'https://en.wikipedia.org/wiki/{page_name}'
    print(f'get {url}')

    # url으로 get 요청을 보내고, 응답을 받습니다
    rep = sess.get(url)
    # 응답으로 온 html을 BeautifulSoup을 이용해 파싱합니다
    bs = BeautifulSoup(rep.text, 'html.parser')
    # a 태그(<a>)를 모두 찾아서 반복합니다
    for link in bs.findAll('a'):
        # a 태그에 href 속성이 있다면
        if 'href' in link.attrs:
            href = link.attrs['href']
            # 만약 href의 앞 6글자가 /wiki/이고, 나머지가 pages에 없다면
            if href[:6] == '/wiki/' and not href[6:] in pages:
                # /wiki/를 제외한 나머지를 pages의 맨 뒤에 추가합니다
                pages.append(href[6:])


def main():
    num = 1000

    with requests.Session() as sess:
        # 수집된 페이지의 수가 num보다 커질 때까지 반복합니다.
        while len(pages) < num:
            # 얼마나 수집되었는지 보여줍니다
            print(f'progress: {len(pages) / num * 100:.1f}%')
            # pages에서 무작위로 하나를 골라, get_page를 호출합니다
            get_page(sess, random.choice(pages))
            # 너무 많은 요청을 보내면 안 되니, 0.5초의 딜레이를 넣어줍니다
            time.sleep(0.5)

    # 수집된 pages를 pages.txt에 저장합니다
    with open('pages.txt', 'w') as f:
        f.write('\n'.join(pages))


if __name__ == '__main__':
    main()
