class Goods():
    def __int__(self, goodsName: str, goodsPrice: int, goodsRate: int):
        self.goodsName = goodsName    # Название товара
        self.goodsPrice = goodsPrice  # Цена товара
        self.goodsRate = goodsRate    # Рейтинг товара

        with open('goods.txt', 'r', encoding='utf-8') as file:
            print(file.read())


