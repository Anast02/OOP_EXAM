class Basket:
    """
    Класс Корзина
    """

    def __init__(self, goodsName=str, goodsPrice=float, goodsAmount=int, total=0):
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.goodsAmount = goodsAmount
        self.total = total
        self.items = []


def sum_busket(goodsPrice, goodsAmount):
    total = 0
    return goodsPrice * goodsAmount
print(f'Сумма товаров в корзине: ' + total)