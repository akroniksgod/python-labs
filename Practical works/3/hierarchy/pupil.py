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
    Возвращает строку с данными о школьнике.
    """
    def __str__(self):
        parent_info = super().__str__()
        return f'{parent_info},' \
               f' из школы {self._school_name},' \
               f' в {self._year} классе'

    """
    Возвращает строку для отладки.
    """
    def __repr__(self):
        parent_info = super().__repr__()
        return f'{parent_info}\n' \
               f'Школа: {self._school_name};\n' \
               f'Класс: {self._year};'
