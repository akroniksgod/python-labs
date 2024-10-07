from __future__ import annotations
from dataclasses import dataclass
import json

"""
Задача.
"""
@dataclass
class Task:
    """
    Название задачи.
    """
    __name: str

    """
    Подробное описание.
    """
    __description: str

    '''
    Категория.
    '''
    __category: str

    """
    Задача решена или нет.
    """
    __checked: bool

    """
    Возвращает представление объекта в виде строки.
    """
    def __str__(self) -> str:
        category = f' #{self.__category}'
        return (f'[{'x' if self.__checked else ' '}] '
                f'{self.__name}'
                f'{category if len(self.__category) > 0 else ''}')

    """
    Возвращает результат проверки на равенство объектов.
    """
    def __eq__(self, other: Task) -> bool:
        is_same_name: bool = self.__name == other.__name
        is_same_description: bool = self.__description == other.__description
        is_same_category: bool = self.__category == other.__category
        is_same_checked: bool = self.__checked == other.__checked
        return is_same_name and is_same_description and is_same_checked and is_same_category

    """
    Возвращает результат проверки на неравенство объектов.
    """
    def __ne__(self, other: Task) -> bool:
        return not self.__eq__(other)

    """
    Возвращает название задачи. 
    """
    def get_name(self) -> str:
        return self.__name

    """
    Возвращает описание задачи. 
    """
    def get_description(self) -> str:
        return self.__description

    """
    Возвращает флаг задачи. 
    """
    def get_checked(self) -> bool:
        return self.__checked

    """
    Возвращает описание категорию. 
    """
    def get_category(self) -> str:
        return self.__category

    """
    Сохраняет название задачи. 
    """
    def set_name(self, name: str) -> None:
        self.__name = name

    """
    Сохраняет описание задачи. 
    """
    def set_description(self, description: str) -> None:
        self.__description = description

    """
    Сохраняет флаг задачи.
    """
    def set_checked(self, checked: bool) -> None:
        self.__checked = checked

    """
    Сохраняет категорию задачи. 
    """
    def set_category(self, category: str) -> None:
        self.__category = category

    '''
    Возвращает словарь для преобразования в json.
    '''
    def to_dict(self) -> dict:
        return {
            "name": self.__name,
            "description": self.__description,
            "checked": self.__checked,
            "category": self.__category,
        }

    '''
    Возвращает объект класса Задача из словаря.
    '''
    @staticmethod
    def from_dict(dict_task: dict) -> Task:
        return Task(
            dict_task['name'],
            dict_task['description'],
            dict_task['category'],
            dict_task['checked'],
        )

    '''
    Сохраняет задачу в файл json.
    !!! Нужен только для тестов.
    '''
    def _save(self) -> None:
        with open('json_task_' + self.__name, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=4)

    '''
    Загружает задачу из файла json.
    !!! Нужен только для тестов.
    '''
    @staticmethod
    def _load(file_name: str) -> Task:
        with open(file_name, 'r', encoding='utf-8') as f:
            json_task = json.load(f)
            return Task.from_dict(json_task)
