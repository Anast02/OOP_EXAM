"""
Модуль для работы с товаром
"""

class Goods:
    """Тип данных Товар"""
    def __init__(self, goodsName: str, goodsPrice: int, goodsRate: int):
        self.goodsName = goodsName    # Название товара
        self.goodsPrice = goodsPrice  # Цена товара
        self.goodsRate = goodsRate    # Рейтинг товара
        if not isinstance(goodsPrice, str):
            raise TypeError("Неверный тип данных")