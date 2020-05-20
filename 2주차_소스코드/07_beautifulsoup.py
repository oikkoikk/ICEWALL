from bs4 import BeautifulSoup

# BeautifulSoup 설명을 위해, 적절한 html 파일을 읽어 html에 넣는다
with open('beautifulsoup.html', 'r', encoding='UTF8') as f:
    html = f.read()

# html = requests.get(url).text
bs = BeautifulSoup(html, 'html.parser')

# findAll을 이용해 태그를 선택할 수 있다.
div = bs.findAll('div')
print(f'div: {div}\n')

# 태그의 속성들은 attrs에 저장되어있다
div0_id = div[0].attrs['id']
print(f'div0_id: {div0_id}\n')


# 태그가 어떤 속성을 갖고 있는지 확인하려면, 아래처럼 in을 쓰면 된다
print('id' in div[0].attrs)
print('invalid_attrs' in div[0].attrs)
print()

# findAll은 유연해서 여러 방식으로 응용할 수 있다
# title, li 태그를 모두 선택한다
print(bs.findAll({'title', 'li'}))
print()

# id가 title인 div를 선택한다
index = bs.findAll('div', {'id': 'container'})[0]

# 해당되는 태그가 하나 뿐일 경우, .태그명 해서 선택할 수도 있다
print(index.p.text)
# 목차를 가져와 내용물을 출력한다
for idx, li in enumerate(index.findAll('li')):
    print(f'{idx}. {li.text}')
