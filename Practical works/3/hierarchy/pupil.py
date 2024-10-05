from __future__ import annotations
from dataclasses import dataclass
from person import Person

"""
Ученик.
"""
@dataclass
class Pupil(Person):
    """
    Наименование школы.
    """
    _school_name: str

    """
    Класс или год обучения.
    """
    _year: int

    """
    Сохраняет название школы.
    """
    def set_school_name(self, school_name: str) -> None:
        if not isinstance(school_name, str):
            pass
        self._school_name = school_name

    """
    Сохраняет год обучения.
    """
    def set_year(self, year: int) -> None:
        if not isinstance(year, int):
            pass
        self._year = year

    """
    Возвращает строку с данными о школьнике.
    """
    def __str__(self) -> str:
        parent_info = super().__str__()
        return f'{parent_info},' \
               f' из школы {self._school_name},' \
               f' в {self._year} классе'

    """
    Возвращает строку для отладки.
    """
    def __repr__(self) -> str:
        parent_info = super().__repr__()
        return f'{parent_info}\n' \
               f'Школа: {self._school_name};\n' \
               f'Класс: {self._year};'

    """
    Перегрузка оператора сравнения.
    """
    def __eq__(self, other: Pupil) -> bool:
        if not isinstance(other, Pupil):
            return False
        is_parent_equal: bool = super().__eq__(other)
        is_same_school: bool = self._school_name == other._school_name
        is_same_year: bool = self._year == other._year
        return is_parent_equal and is_same_school and is_same_year

    """
    Перегрузка оператора сравнения на неравенство.
    """
    def __ne__(self, other: Pupil) -> bool:
        if not isinstance(other, Pupil):
            return False
        return not self.__eq__(other)

    """
    Перегрузка оператора меньше.
    """
    def __lt__(self, other: Pupil) -> bool:
        if not isinstance(other, Pupil):
            return False
        return self._age < other._age

    """
    Перегрузка оператора больше.
    """
    def __gt__(self, other: Pupil) -> bool:
        if not isinstance(other, Pupil):
            return False
        return self._age > other._age

    """
    Перегрузка оператора меньше или равно.
    """
    def __le__(self, other: Pupil) -> bool:
        if not isinstance(other, Pupil):
            return False
        return self._age <= other._age

    """
    Перегрузка оператора больше или равно.
    """
    def __ge__(self, other: Pupil) -> bool:
        if not isinstance(other, Pupil):
            return False
        return self._age >= other._age
