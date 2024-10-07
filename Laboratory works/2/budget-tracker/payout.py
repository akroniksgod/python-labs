from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal

"""
Выплата.
"""
@dataclass
class Payout:
    """
    Название выплаты.
    """
    __name: str

    """
    Стоимость.
    """
    __amount: Decimal

    '''
    Категория.
    '''
    __category: str

    """
    Подробное описание.
    """
    __description: str

    """
    Возвращает представление объекта в виде строки.
    """
    def __str__(self) -> str:
        category = f' #{self.__category}'
        return (f'{self.__name}, '
                f'{self.__amount:.3f} руб. '
                f'{category if len(self.__category) > 0 else ''}')

    """
    Возвращает результат проверки на равенство объектов.
    """
    def __eq__(self, other: Payout) -> bool:
        is_same_name: bool = self.__name == other.__name
        is_same_amount: bool = self.__amount == other.__amount
        is_same_category: bool = self.__category == other.__category
        is_same_description: bool = self.__description == other.__description
        return is_same_name and is_same_amount and is_same_category and is_same_description

    """
    Возвращает результат проверки на неравенство объектов.
    """
    def __ne__(self, other: Payout) -> bool:
        return not self.__eq__(other)

    """
    Возвращает название выплаты. 
    """
    def get_name(self) -> str:
        return self.__name

    """
    Возвращает сумму выплаты. 
    """
    def get_amount(self) -> Decimal:
        return self.__amount

    """
    Возвращает категорию выплаты. 
    """
    def get_category(self) -> str:
        return self.__category

    """
    Возвращает описание выплаты. 
    """
    def get_description(self) -> str:
        return self.__description

    """
    Сохраняет название выплаты. 
    """
    def set_name(self, name: str) -> None:
        self.__name = name

    """
    Сохраняет сумму выплаты.
    """
    def set_amount(self, amount: str | Decimal) -> None:
        self.__amount = amount if isinstance(amount, Decimal) else Decimal(amount)

    """
    Сохраняет категорию выплаты. 
    """
    def set_category(self, category: str) -> None:
        self.__category = category

    """
    Сохраняет описание выплаты. 
    """
    def set_description(self, description: str) -> None:
        self.__description = description

    '''
    Возвращает словарь для преобразования в json.
    '''
    def to_dict(self) -> dict:
        return {
            "name": self.__name,
            "amount": str(self.__amount),
            "category": self.__category,
            "description": self.__description,
        }

    '''
    Возвращает объект класса Выплата из словаря.
    '''
    @staticmethod
    def from_dict(dict_task: dict) -> Payout:
        return Payout(
            dict_task['name'],
            Decimal(dict_task['amount']),
            dict_task['category'],
            dict_task['description'],
        )
