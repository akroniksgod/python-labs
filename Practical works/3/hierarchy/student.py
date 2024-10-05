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
    __group_name: str

    """
    Название специальности.
    """
    __major_name: str

    """
    Возвращает строку с данными о студенте.
    """
    def __str__(self):
        parent_info = super().__str__()
        return f'{parent_info},' \
               f' из группы {self.__group_name},' \
               f' по специальности {self.__major_name}'

    """
    Возвращает строку для отладки.
    """
    def __repr__(self):
        parent_info = super().__repr__()
        return f'{parent_info}\n' \
               f'Группа: {self.__group_name};\n' \
               f'Специальность: {self.__major_name};'
