class Dogs:
    """"Класс, описывающий собак"""
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Собаку зовут {self.name}. Ей {self.age}.'
        """ Данный метод описывает самые базовые характеристики любой собаки - ее имя и возраст.  """

class Corgi(Dogs):
    """ Дочерний класс, описывающий породу 'Корги'"""
    def __init__(self, name: str, age: int, height: int, weight: int) :
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self) -> str:
        return f'Корги зовут {self.name}. Ей {self.age}. Рост Корги - {self.height}. Вес корги - {self.weight}.'
        """Данный метод описывает базовые характеристики 'Корги'. 
        Перегрузка этого метода необходима, чтобы указать рост и вес. """

if __name__ == "__main__":
    # Write your solution here
    pass
