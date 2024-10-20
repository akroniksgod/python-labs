from __future__ import annotations
from dataclasses import dataclass
from pupil import Pupil

"""
Ученик.
"""
@dataclass
class Student(Pupil):
    """
    Наименование группы.
    """
    _group_name: str

    """
    Название специальности.
    """
    _major_name: str

    """
    Сохраняет название группы.
    """
    def set_school_name(self, group_name: str) -> None:
        if not isinstance(group_name, str):
            pass
        self._group_name = group_name

    """
    Сохраняет название специальности.
    """
    def set_major_name(self, major_name: str) -> None:
        if not isinstance(major_name, str):
            pass
        self._major_name = major_name

    """
    Возвращает строку с данными о студенте.
    """
    def __str__(self) -> str:
        return f'{self._surname} {self._name},' \
               f' {"мужчина" if self._gender else "женщина"},' \
               f' {self._age} лет,' \
               f' в ВУЗе {self._school_name},' \
               f' на {self._year} курсе,' \
               f' из группы {self._group_name},' \
               f' по специальности {self._major_name}'

    """
    Возвращает строку для отладки.
    """
    def __repr__(self) -> str:
        return f'Фамилия: {self._surname};\n' \
               f'Имя: {self._name};\n' \
               f'Пол: {"мужчина" if self._gender else "женщина"};\n' \
               f'Возраст: {self._age} лет;\n' \
               f'ВУЗ: {self._school_name};\n' \
               f'Курс: {self._year};\n' \
               f'Группа: {self._group_name};\n' \
               f'Специальность: {self._major_name};'

    """
    Перегрузка оператора сравнения.
    """
    def __eq__(self, other: Student) -> bool:
        if not isinstance(other, Student):
            return False
        is_parent_equal: bool = super().__eq__(other)
        is_same_group: bool = self._group_name == other._group_name
        is_same_major: bool = self._major_name == other._major_name
        return is_parent_equal and is_same_group and is_same_major

    """
    Перегрузка оператора сравнения на неравенство.
    """
    def __ne__(self, other: Student) -> bool:
        if not isinstance(other, Student):
            return False
        return not self.__eq__(other)

    """
    Перегрузка оператора меньше.
    """
    def __lt__(self, other: Student) -> bool:
        if not isinstance(other, Student):
            return False
        return self._age < other._age

    """
    Перегрузка оператора больше.
    """
    def __gt__(self, other: Student) -> bool:
        if not isinstance(other, Student):
            return False
        return self._age > other._age

    """
    Перегрузка оператора меньше или равно.
    """
    def __le__(self, other: Student) -> bool:
        if not isinstance(other, Student):
            return False
        return self._age <= other._age

    """
    Перегрузка оператора больше или равно.
    """
    def __ge__(self, other: Student) -> bool:
        if not isinstance(other, Student):
            return False
        return self._age >= other._age
