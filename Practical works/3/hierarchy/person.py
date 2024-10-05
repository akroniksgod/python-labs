from dataclasses import dataclass

"""
Человек.
"""
@dataclass
class Person:
    """
    Имя.
    """
    _name: str

    """
    Фамилия.
    """
    _surname: str

    """
    Возраст.
    """
    _age: int

    """
    Пол.
    """
    _gender: bool

    """
    Возвращает строку с данными о персоне.
    """
    def __str__(self):
        return f'{self._surname} {self._name},' \
               f' {"мужчина" if self._gender else "женщина"},' \
               f' {self._age} лет'

    """
    Возвращает строку для отладки.
    """
    def __repr__(self):
        return f'Фамилия: {self._surname};\n' \
               f'Имя: {self._name};\n' \
               f'Пол: {"мужчина" if self._gender else "женщина"};\n' \
               f'Возраст: {self._age} лет;'
