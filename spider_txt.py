#-*-coding:utf-8_*_
#作者      :71460
#创建时间  :2019/3/26 15:55
#文件      :spider_txt.py
#IDE       :PyCharm
import requests
import bs4
def open_url(url):
    web_url = url
    res = requests.get(web_url)
    res.encoding = "utf-8"
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    return soup
def targets(soup):
    targets = soup.find_all("div",class_="menu")
    return targets
def fin_urls(soup):
    links = soup.find_all('a')
    url_lst = []
    fin_url = []
    for item in links:
        url = item.get('href')
        url_lst.append(url)
    for urls in url_lst:
        str2 = 'http://demo.pythoner.com/itt2zh' + urls[1:10]
        if str2 not in fin_url:
            fin_url.append(str2)
    return fin_url
def article(web_url):
    res = requests.get(web_url)
    res.encoding = "utf-8"
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    article = soup.find_all("div", class_="article")
    return article
def mian():
    url = "http://demo.pythoner.com/itt2zh/"
    soup = open_url(url)
    target = targets(soup)
    fin_url = fin_urls(soup)
    with open("book.txt","w",encoding="utf-8") as f:
        for each in target:
            f.write(str(each.ul.text))
        for each in fin_url:
            articles = article(each)
            for each in articles:
                f.write(str(each.text))
    f.close()
if __name__ == '__main__':
    mian()

