import requests
from bs4 import BeautifulSoup
import urllib.parse
import product as p
import re
# Webページを取得して解析する

def excute(str):
    word = str
    load_url = "https://www.nike.com/jp/w?q="+word+"&vst="+word
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    items=soup.select("div[class='product-card__body']")

    n=1
    products = []
    for item in items:
        img=item.find('img')
        title = img['alt']
        price = ""
        if item.find('.product-price') is None:
            price =item.select_one('.product-price').text.replace('\n','').replace(' ','').replace('	','')
        #数値だけ取り出す
        price = re.sub(r"\D", "", price)

        n+=1
        a = item.select_one('a')
        url = a['href']
        product = p.Product(title,price,url,"nike")
        products.append(product)

    return products
