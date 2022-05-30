class Category():
    def __init__(self, num_category: int, name_category: str, list_of_goods):
        self.num_category = num_category     # Номер категории
        self.name_category = name_category   # Название категории
        self.list_of_goods = []              # Список товаров категории
