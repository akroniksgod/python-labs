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
    __card_number: str

    """
    Возвращает строку с данными о студенте заочнике.
    """
    def __str__(self):
        parent = super().__str__()
        return f"{parent}," \
               f" с зачётной книжкой {self.__card_number}"

    """
    Возвращает строку для отладки.
    """
    def __repr__(self):
        parent = super().__repr__()
        return f"{parent}\n" \
               f"Номер зачётной книжки: {self.__card_number}.\n"
