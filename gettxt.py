import requests
from lxml import etree
from time import sleep
import random
w = 'https://www.biqiugexx.com/'
url = 'https://www.biqiugexx.com/book_32201/'
urlget = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'})
urlget.encoding = urlget.apparent_encoding
xp1 = etree.HTML(urlget.text)
chapter = xp1.xpath("//dd/a/@href")
name = xp1.xpath("//dd/a[@href]/text()")
l = len(chapter)
# print(l)
save = ''
for i, j in zip(chapter[12:l], name[12:l]):  # len(chapter)
    url_chapter = 'https://www.biqiugexx.com/'+i
    print('「章节名字」',j,'「章节链接」',url_chapter)
    get_chapter = requests.get(url_chapter, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'})
    get_chapter.encoding = get_chapter.apparent_encoding
    xp2 = etree.HTML(get_chapter.text)
    txt = xp2.xpath('//div[@class="showtxt"]/text()')
    strtxt = "".join(txt)
    strtxt = j+strtxt
    # print('「正在保存文本内容……')  # ,strtxt)
    # with open(f'./书剑长安/{j}.txt', 'w', encoding='utf-8') as f:
    #     f.write(strtxt)
    save += strtxt
    print(' END')
    ran = random.randint(5,12)
    sleep(ran/10)

with open(f'./书剑长安.txt', 'w', encoding='utf-8') as f:
    f.write(save)

