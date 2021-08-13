class Product:

    def __init__(self, title, price,url,brand):
        self.title = title
        self.price = price
        self.url = url
        self.brand = brand

    def __lt__(self, other):  # 自作クラスで大小を判別するための関数
        return self.price < other.price
