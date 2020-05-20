import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/w/index.php?search=pthon'
results = []

with requests.Session() as sess:
    print("start")
    rep = sess.get(url)
    bs = BeautifulSoup(rep.text, 'html.parser')
    for tagss in bs.findAll('a'):
        if 'data-serp-pos' in tagss.attrs and 'href' in tagss.attrs:
            href = tagss.attrs['href']
            if href[:6] == '/wiki/':
                results.append(href[6:])
                print(href[6:])

with open('result.txt', 'w') as f:
        f.write('\n'.join(results))
print("fin", end='')
    
    