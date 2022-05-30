from utils.category import Category


class Goods():
    def __int__(self, goodsName: str, goodsPrice: [int, float], goodsRate: int):
        self.goodsName = goodsName    # Название товара
        self.goodsPrice = goodsPrice  # Цена товара
        self.goodsRate = goodsRate    # Рейтинг товара


