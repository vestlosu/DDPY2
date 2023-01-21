class Gym:
    """
    Этот класс описывает модель тренажерного зала.
    """
    def __init__(self):
        self.set = 5
        self.jock = 10

    def pump_muscles(self, done_sets) -> int:
        """
        Метод увеличивает количество сделанных подходов
        :return: Количество сделанных подходов

        """
        if not isinstance(done_sets, int):
            raise TypeError("Количество подходов должно быть типа int")
        if done_sets < 0:
            raise ValueError("Количество подходов не может быть меньше 0")

        self.set += done_sets

    def amount_of_jocks(self) -> int:
        """
        Метод, считающий качков в зале
        :return: Количество качков в зале на данный момент

        """
        ...



class Instagram:
    """
    Данный класс описывает модель инстаграмма
    """
    def __init__(self):
        self.followers = 200
        self.subscriptions = 100

    def followers_increase(self, amount_of_followers) -> int:
        """
        Метод увеличивает число подписчиков
        :return: показывает текущее количество подписчиков

        """
        if not isinstance(amount_of_followers,int):
            raise TypeError("Количество подписчиков должно быть типа int")
        ...

    def subscriptions_increase(self, amount_of_subscriptions) -> int:
        """
         Метод увеличивает число подписок
        :return: показывает текущее аоличество подписок
        """
        if not isinstance(amount_of_subscriptions, int):
            raise TypeError("Количество подписок должно быть типа int")
        ...

class Parking:
    """
Данный метод описывает модель парковки

    """
    def __init__(self):
        self.cars = 400
        self.vacant_places = 1000

    def is_place_vacant(self)-> bool:
        """
        Метод показывает, занято ли парковочное место
        :return: Занято ли парковочное место

        """
        ...
    def vacant_places_amount(self) -> int:
        """
        Метод показывает остаток свободных мест на парковке
        :return: Количество свободных мест на парковке
        """
        ...
if __name__  == "__main__":
    import doctest
    doctest.testmod()

