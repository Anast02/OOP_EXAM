class Basket:
    """Тип данных Корзина"""
    def __init__(self, goodsName: str, goodsPrice: int):
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice


    def sum_basket(self):
        basket_list = list(self.values())
        print(f'В корзине  {len(self)} шт. товара на сумму: {sum(basket_list)}')