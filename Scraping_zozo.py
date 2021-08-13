import requests
import product as p
from bs4 import BeautifulSoup
import urllib.parse
import re
# Webページを取得して解析する

def excute(str):
    word = urllib.parse.quote(str, encoding='shift-jis')
    load_url = "https://zozo.jp/search/?p_keyv="+word
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    items=soup.select("li[class='o-grid-catalog__item']")

    n=1

    products = []
    for item in items:
        img=item.find('img')
        title = img['alt']
        price = ""
        if item.select_one('.c-catalog-body__price') is None:
            price =item.select_one('.c-catalog-body__price--discount').text
        else:
            price =item.select_one('.c-catalog-body__price').text
        #数値だけ取り出す
        price = re.sub(r"\D", "", price)

        url = ""
        if not(item.select_one('.c-catalog-header__link') is None):
            a = item.select_one('.c-catalog-header__link')
            url = a['href']
            if url[0:5] != "https":
                url = "https://zozo.jp"+url
        n+=1
        product = p.Product(title,price,url,"zozo")
        products.append(product)

    return products
