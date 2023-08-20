import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.join('/', 'Users', 'Максим', 'PycharmProjects',
                            'electronics-shop-project-home-work', 'src', 'items.csv')

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) > 10:
            self.__name = new_name
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """instantiation of class Item with data from items.csv file"""
        cls.all = []
        with open(cls.CSV_PATH) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    cls(
                        (row['name']),
                        cls.string_to_number(row['price']),
                        cls.string_to_number(row['quantity'])
                    )
                except FileNotFoundError:
                    print('Error, could not find the value')

    @staticmethod
    def string_to_number(num_str) -> int:
        """returns int from str number"""
        return int(float(num_str))
