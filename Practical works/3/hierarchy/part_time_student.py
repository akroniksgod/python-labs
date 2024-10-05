from __future__ import annotations
from dataclasses import dataclass
from student import Student

"""
Студент заочник.
"""
@dataclass
class PartTimeStudent(Student):
    """
    Номер зачётной книжки.
    """
    _card_number: str

    """
    Возвращает строку с данными о студенте заочнике.
    """
    def __str__(self) -> str:
        parent = super().__str__()
        return f"{parent}," \
               f" с зачётной книжкой {self._card_number}"

    """
    Возвращает строку для отладки.
    """
    def __repr__(self) -> str:
        parent = super().__repr__()
        return f"{parent}\n" \
               f"Номер зачётной книжки: {self._card_number}.\n"

    """
    Перегрузка оператора сравнения.
    """
    def __eq__(self, other: PartTimeStudent) -> bool:
        if not isinstance(other, PartTimeStudent):
            return False
        is_parent_equal: bool = super().__eq__(other)
        is_same_card: bool = self._card_number == other._card_number
        return is_parent_equal and is_same_card

    """
    Перегрузка оператора сравнения на неравенство.
    """
    def __ne__(self, other: PartTimeStudent) -> bool:
        if not isinstance(other, PartTimeStudent):
            return False
        return not self.__eq__(other)

    """
    Перегрузка оператора меньше.
    """
    def __lt__(self, other: PartTimeStudent) -> bool:
        if not isinstance(other, PartTimeStudent):
            return False
        return self._age < other._age

    """
    Перегрузка оператора больше.
    """
    def __gt__(self, other: PartTimeStudent) -> bool:
        if not isinstance(other, PartTimeStudent):
            return False
        return self._age > other._age

    """
    Перегрузка оператора меньше или равно.
    """
    def __le__(self, other: PartTimeStudent) -> bool:
        if not isinstance(other, PartTimeStudent):
            return False
        return self._age <= other._age

    """
    Перегрузка оператора больше или равно.
    """
    def __ge__(self, other: PartTimeStudent) -> bool:
        if not isinstance(other, PartTimeStudent):
            return False
        return self._age >= other._age
