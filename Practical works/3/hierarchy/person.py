from dataclasses import dataclass

"""
Человек.
"""
@dataclass
class Person:
    """
    Имя.
    """
    __name: str

    """
    Фамилия.
    """
    __surname: str

    """
    Возраст.
    """
    __age: int

    """
    Пол.
    """
    __gender: bool

    """
    Возвращает строку с данными о персоне.
    """
    def __str__(self):
        return f'{self.__surname} {self.__name},' \
               f' {"мужчина" if self.__gender else "женщина"},' \
               f' {self.__age} лет'

    """
    Возвращает строку для отладки.
    """
    def __repr__(self):
        return f'Фамилия: {self.__surname};\n' \
               f'Имя: {self.__name};\n' \
               f'Пол: {"мужчина" if self.__gender else "женщина"};\n' \
               f'Возраст: {self.__age} лет;'
