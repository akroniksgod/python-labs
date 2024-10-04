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
    __school_name: str

    """
    Класс или год обучения.
    """
    __year: int

    """
    Возвращает строку с данными о персоне.
    """
    def __str__(self):
        parent_info = super().__str__()
        return f'{parent_info},' \
               f' из школы {self.__school_name},' \
               f' в {self.__year} классе.'

    """
    Возвращает строку для отладки.
    """
    def __repr__(self):
        parent_info = super().__repr__()
        return f'{parent_info}\n' \
               f'Школа: {self.__school_name};\n' \
               f'Класс: {self.__year};'
