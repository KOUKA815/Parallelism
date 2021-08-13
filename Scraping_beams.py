import requests
from bs4 import BeautifulSoup
import urllib.parse
import product as p
import re
# Webページを取得して解析する

def excute(str):
    word = str
    load_url = "https://www.beams.co.jp/search/?q="+word+"&search=true&sort=-sum_qty_w"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    items=soup.select("li[class='beams-list-image-item']")


    n=1
    products = []
    for item in items:
        title = item.select_one('.product-name').text.replace('\r\n','').replace(' ','').replace('	','')
        price = ""
        if item.select_one('.sale') is None:
            price =item.select_one('.price').text.replace('\r\n','').replace(' ','').replace('	','')
        else:
            price =item.select_one('.sale').text.replace('\r\n','').replace(' ','').replace('	','')
        #数値だけ取り出す
        if price.find("[") != -1:
            price = price[0:price.find("[")]
        price = re.sub(r"\D", "", price)

        a = item.select_one('a')
        url = "https://www.beams.co.jp"+a['href']
        n+=1
        product = p.Product(title,price,url,"beams")
        products.append(product)

    return products
