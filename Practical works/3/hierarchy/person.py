from __future__ import annotations
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
    Сохраняет имя.
    """
    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            pass
        self._name = name

    """
    Сохраняет фамилию.
    """
    def set_surname(self, surname: str) -> None:
        if not isinstance(surname, str):
            pass
        self._surname = surname

    """
    Сохраняет возраст.
    """
    def set_age(self, age: int) -> None:
        if not isinstance(age, int):
            pass
        self._age = age

    """
    Сохраняет пол.
    """
    def set_gender(self, gender: bool) -> None:
        res: bool = gender
        if isinstance(gender, str):
            gen = gender.lower()
            res = gen == 'm' or gen == 'м' or gen == 'муж'
        elif not isinstance(gender, bool):
            pass
        self._gender = res

    """
    Возвращает строку с данными о персоне.
    """
    def __str__(self) -> str:
        return f'{self._surname} {self._name},' \
               f' {"мужчина" if self._gender else "женщина"},' \
               f' {self._age} лет'

    """
    Возвращает строку для отладки.
    """
    def __repr__(self) -> str:
        return f'Фамилия: {self._surname};\n' \
               f'Имя: {self._name};\n' \
               f'Пол: {"мужчина" if self._gender else "женщина"};\n' \
               f'Возраст: {self._age} лет;'

    """
    Перегрузка оператора сравнения.
    """
    def __eq__(self, other: Person) -> bool:
        if not isinstance(other, Person):
            return False
        is_same_name: bool = self._name == other._name
        is_same_surname: bool = self._surname == other._surname
        is_same_age: bool = self._age == other._age
        is_same_gender: bool = self._gender == other._gender
        return is_same_name and is_same_surname and is_same_age and is_same_gender

    """
    Перегрузка оператора сравнения на неравенство.
    """
    def __ne__(self, other: Person) -> bool:
        if not isinstance(other, Person):
            return False
        return not self.__eq__(other)

    """
    Перегрузка оператора меньше.
    """
    def __lt__(self, other: Person) -> bool:
        if not isinstance(other, Person):
            return False
        return self._age < other._age

    """
    Перегрузка оператора больше.
    """
    def __gt__(self, other: Person) -> bool:
        if not isinstance(other, Person):
            return False
        return self._age > other._age

    """
    Перегрузка оператора меньше или равно.
    """
    def __le__(self, other: Person) -> bool:
        if not isinstance(other, Person):
            return False
        return self._age <= other._age

    """
    Перегрузка оператора больше или равно.
    """
    def __ge__(self, other: Person) -> bool:
        if not isinstance(other, Person):
            return False
        return self._age >= other._age
