from __future__ import annotations
from typing import List, Dict
from attr import dataclass

'''
Страна.
'''
@dataclass
class Country:
    '''
    Название.
    '''
    name: str

    '''
    Столица.
    '''
    capital: str

    '''
    Языки.
    '''
    languages: List[str]

    '''
    Население.
    '''
    population: int

    '''
    Флаг.
    '''
    flag: str

    '''
    Валюта.    
    '''
    currency: str

    '''
    Перегрузка метода получения строчного представления класса.
    '''
    def __str__(self):
        return (f"\tНазвание: {self.name};"
                f" Столица: {self.capital};"
                f" Языки: {self.languages};"
                f" Население: {self.population};"
                f" Флаг: {self.flag};"
                f" Валюта: {self.currency}.")

    '''
    Функция для преобразования словаря в экземпляр класса Country
    '''
    @staticmethod
    def dict_to_country(d: Dict) -> Country:
        return Country(
            name=d['name'],
            capital=d['capital'],
            languages=d['languages'],
            population=d['population'],
            flag=d['flag'],
            currency=d['currency']
        )
