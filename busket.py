class Basket:
    def __init__(self, goodsName:str, goodsPrice:int, goodsAmount:int, total:int, add_to_basket:int):
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.goodsAmount = goodsAmount
        self.total = total
        self.init_add_to_basket(add_to_basket)
        self.items = []

    def add_to_basket(self, goodsName=str):
        self.goodsName = goodsName

    @staticmethod
    def sum_basket(goodsPrice, goodsAmount):
        total = 0
        return goodsPrice * goodsAmount