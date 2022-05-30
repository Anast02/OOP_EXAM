from utils.category import Category


class Goods():
    def __int__(self, goodsName: str, goodsPrice: [int, float], goodsRate: int):
        self.goodsName = goodsName    # Название товара
        self.goodsPrice = goodsPrice  # Цена товара
        self.goodsRate = goodsRate    # Рейтинг товара

"""
Отображение товаров выбранной категории
"""
def show_items():
    i = 1
    items = {}
    with open('goods.txt', 'r', encoding='utf-8') as file:
        for line in file:
            a = line.split(",")
            if line.split(",")[0] == Category.name_category:
                items_str = Goods(line.split(",")[1], line.split(",")[2], line.split(",")[3])
                items[i] = items_str.goodsName, items_str.goodsPrice, items_str.goodsRate
                print(i, 'Название товара: ', items_str.goodsName, ' ', 'Цена товара: ', items_str.goodsPrice, ' ', 'Рейтинг товара: ', items_str.goodsRate)
                i += 1


