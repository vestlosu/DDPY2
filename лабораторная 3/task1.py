class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга '{self.name}'. Автор '{self.author}'"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.name = name
        self.author = author
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int") 
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self):
        return f"Книга '{self.name}'. Автор '{self.author}'. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.name = name
        self.author = author
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должно быть положительным числом")
        self.duration = duration

    def __str__(self):
        return f"Книга '{self.name}'. Автор '{self.author}'. Продолжительномть: {self.duration}"

print(Book("гОВНО", "ХУЙ"))
print(PaperBook("жопа", "попка", 300))
print(AudioBook("soul", "lol", 444.44))