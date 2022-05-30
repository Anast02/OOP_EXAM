class Basket:
    """
    Класс Корзина
    """

    def __init__(self, goodsName=str, goodsPrice=float, goodsAmount=int, total=int, add_to_busket=int):
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.goodsAmount = goodsAmount
        self.total = total
        self.init_add_to_busket(add_to_busket)
        self.items = []

    def add_to_busket(self, add_to_busket = int):
        self.add_to_busket = add_to_busket


    def sum_busket(goodsPrice, goodsAmount):
        total = 0
        return goodsPrice * goodsAmount
    print(f'Сумма товаров в корзине: {total}')