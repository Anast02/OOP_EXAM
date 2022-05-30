import txt
from dataclasses import dataclass

@dataclass
class Category():
    num_category: int   # Номер категории
    name_category: str  # Название категории
    list_of_goods: list # Список товаров категории

    """"
    Вывод категории товаров
    """

    def choose_category():
        selected_category = input('Выберете категорию: ')


        if selected_category == '1':
            name_category = "Техника для уборки"
            print(name_category)
        elif selected_category == '2':
            name_category = "Техника для кухни"
            print(name_category)
        elif selected_category == '3':
            name_category = "Крупная бытовая техника"
            print(name_category)
        elif selected_category == '4':
            name_category = "Встраиваемая техника"
            print(name_category)
        else:
            print('Упс, такой категории не существует :(')

        """
        Просмотр товаров из выбранной категории
        """
        with open('goods.txt', 'r', encoding='utf-8') as file:
            print(file.read())

        """
        Выбор товара
        """
        item = input('Выберите товар из категории: ')
