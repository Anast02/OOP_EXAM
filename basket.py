class Basket:
    def __init__(self, item_name = None, item_price = None):
        self.item_name = item_name
        self.item_price = item_price

    def sum_basket(self):
        a = list(self.values())
        print("В корзине" , len(self), 'шт. товара на сумму', sum(a))