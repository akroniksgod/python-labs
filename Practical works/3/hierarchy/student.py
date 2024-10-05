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
    Возвращает строку с данными о студенте.
    """
    def __str__(self):
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
    def __repr__(self):
        return f'Фамилия: {self._surname};\n' \
               f'Имя: {self._name};\n' \
               f'Пол: {"мужчина" if self._gender else "женщина"};\n' \
               f'Возраст: {self._age} лет;\n' \
               f'ВУЗ: {self._school_name};\n' \
               f'Курс: {self._year};\n' \
               f'Группа: {self._group_name};\n' \
               f'Специальность: {self._major_name};'
