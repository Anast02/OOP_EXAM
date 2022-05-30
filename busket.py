class Busket:
    def __init__(self, goodsName=str, goodsPrice=int, goodsAmount=int, total=int, add_to_busket=int):
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.goodsAmount = goodsAmount
        self.total = total
        self.init_add_to_busket(add_to_busket)
        self.items = []

    def add_to_busket(self, goodsName=str):
        self.goodsName = goodsName


    def sum_busket(goodsPrice, goodsAmount):
        total = 0
        return goodsPrice * goodsAmount