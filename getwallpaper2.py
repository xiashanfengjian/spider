import requests
from lxml import etree
url = 'https://wallhaven.cc/search?q=id%3A123704&sorting=random&ref=fp&seed=NVkuSt&page=2'
url = 'https://wallhaven.cc/search?q=id%3A968&categories=010&purity=110&sorting=relevance&order=desc&page=3'
urlget = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'})
urlget.encoding = 'gbk '
print(urlget.text)
xp = etree.HTML(urlget.text)
img_urls = xp.xpath('//ul/li/figure/a/@href')
print(img_urls)
for u in img_urls:
    print(f'地址:{u}')
    img_resp = requests.get(u, headers={'User-Agent ': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'})
    xxp = etree.HTML(img_resp.text)
    imgurl = xxp.xpath('//div/img/@src')
    print(imgurl)
    n = xxp.xpath('//img/@alt')
    print(n)
    img = requests.get(imgurl[-1], headers={'User-Agent ': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'})
    with open(f'./imgwall/{n[-1]}.png', 'wb') as f:
        f.write(img.content)

# https://wallhaven.cc/search?q=id%3A123704&categories=111&purity=100&atleast=2560x1080&ratios=portrait%2C16x9&sorting=random&order=desc&page=3
# 网址+q=“搜索词”+categories(特征：3个1代表三个特征的开关：General,Anime,People)+purity(特征：前2个1代表两个特征的开关，第三个未知：SFM,Skechy)+atleast(分辨率)+ratios(ratios=portrait%2C16x9)+排序方式+未知+page
