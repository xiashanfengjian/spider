import requests
import rich
from lxml import etree
from time import sleep
import random

def content(key,time1,time2,m):
    # w2 = 'https://xs.zidianzhan.net/scholar?start='+'10'+'&q='+'dynamics+of+droplet+impact'+'&hl=zh-CN&as_sdt=0,5&as_ylo='+'2010'+'&as_yhi='+'2022'

    for j in range(m):
        w2 = 'https://xs.zidianzhan.net/scholar?start='+str((j-1)*10)+'&q='+key+'&hl=zh-CN&as_sdt=0,5&as_ylo='+time1+'&as_yhi='+time2
        url = w2
        urlget = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
                                            'Cookie': 'xxxx'})
        urlget.encoding = urlget.apparent_encoding
        xp1 = etree.HTML(urlget.text)
        id_paper = xp1.xpath("//h3[@class='gs_rt']/a/@id")
        id = xp1.xpath('//div[@class="gs_r gs_or gs_scl"]/@data-cid')
        for i,k in zip(id_paper,id):
            name = xp1.xpath("string(//h3[@class='gs_rt']/a[@id='"+i+"'])")
            art = xp1.xpath("string(//div[@data-cid='"+k+"']//div[@class='gs_a'])")
            url_paper = xp1.xpath("//h3[@class='gs_rt']/a[@id='"+i+"']/@href")
            print('!'+'-'*80+'!')
            print(f"\033[31m{str(j*10+id_paper.index(i)+1)}\033[0m",f"\033[32m{name}\033[0m")
            print(f"\033[33m{art}\033[0m")
            print(f"\033[34m{url_paper}\033[0m")
    print(urlget)

# main
key = input('Keyword:')
time1, time2 = input('Range1:'), input('Range2:')
m = int(input('How much:'))
content(key,time1,time2,m)
