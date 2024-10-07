from __future__ import annotations
from payout import Payout
from decimal import Decimal
import json

'''
Название файла, в котором храним список выплат.
'''
json_name: str = 'payouts.json'

"""
Список выплат.
"""
class PayoutList:
    """
    Список выплат.
    """
    __payouts: list[Payout]

    '''
    Суммарные затраты.
    '''
    __total: Decimal

    '''
    Инициализирует список выплат.
    '''
    def __init__(self, payouts: list[Payout] = ()) -> None:
        self.__payouts = payouts
        self.__total = self.get_total_amount()

    '''
    Возвращает строковое представление списка выплат.
    '''
    def __str__(self) -> str:
        payouts: str = ''
        payout_position: int = 1
        for payout in self.__payouts:
            payouts += f'\t{payout_position} {payout.__str__()};\n'
            payout_position += 1
        payouts += f'\tСуммарные затраты: {self.__total:.3f} руб.\n'
        return payouts

    '''
    Выводит список выплат в консоль.
    '''
    def show(self) -> None:
        print('Выплаты:')
        print(self.__str__())

    '''
    Показать список переданный выплат в консоли.
    '''
    @staticmethod
    def show_payouts(payouts: PayoutList) -> None:
        print('Выплаты:')
        print(payouts.__str__())

    '''
    Возвращает список объектов.
    '''
    def _to_dist_list(self) -> list[dict]:
        return [payout.to_dict() for payout in self.__payouts]

    '''
    Сохраняет список выплат в json.
    '''
    def save(self) -> None:
        self.__total = self.get_total_amount()
        with open(json_name, 'w', encoding='utf-8') as f:
            json.dump(self._to_dist_list(), f, indent=4)
            print('Изменения сохранены!\n')

    '''
    Возвращает список выплат.
    '''
    @staticmethod
    def get_saved_payouts(file_name: str) -> list[Payout]:
        with open(file_name) as json_data:
            payout_dict_list: list[dict] = json.load(json_data)
            return list(map(lambda payout: Payout.from_dict(payout), payout_dict_list))

    '''
    Добавляет выплату в список выплат.
    '''
    def append(self, payout: Payout) -> None:
        self.__payouts.append(payout)

    '''
    Добавляет выплату в список выплат.
    '''
    def add(self) -> None:
        print('\nСоздание выплаты')
        name: str = input('\tНазвание: ')
        amount: str = input('\tСумма: ')
        category: str = input('\tКатегория: ')
        description: str = input('\tОписание: ')
        new_payout = Payout(name, Decimal(amount), category, description)
        self.append(new_payout)
        self.save()

    '''
    Редактирует выплату в список выплат.
    '''
    def change(self) -> None:
        print('\nРедактирование выплаты')
        position: str = input('\tВведите номер выплаты: ')
        index: int = int(position) - 1
        if index < 0 or index >= len(self.__payouts):
            print('Не удалось внести изменения!\n')
            return

        payout: Payout = self.__payouts[index]
        print(f'\t{payout}')
        choice: str = input('\t1. Изменить название;\n'
                            '\t2. Изменить сумму выплаты;\n'
                            '\t3. Изменить категорию.\n'                       
                            '\t4. Изменить описание;\n'
                            '\t>')
        new_value: str = input('\tНовое значение: ')
        options: dict = {
            '1': payout.set_name,
            '2': payout.set_amount,
            '3': payout.set_category,
            '4': payout.set_description,
        }
        options[choice](new_value)
        self.save()

    '''
    Удаляет выплату из списка выплат по названию.
    '''
    def _remove_payout_by_name(self) -> None:
        name: str = input('\n\tНазвание: ').lower()
        self.__payouts = filter(lambda x: str(x.name).lower() == name, self.__payouts)

    '''
    Удаляет выплату из списка выплат по индексу.
    '''
    def _remove_payout_by_index(self) -> None:
        position: str = input('\n\tНомер: ')
        index: int = int(position) - 1
        self.__payouts.pop(index)

    '''
    Удаляет выплату из списка выплат.
    '''
    def remove(self) -> None:
        print('\nУдаление выплаты')
        choice: str = input('\t1. Удалить по номеру;\n'
                            '\t2. Удалить по названию.\n'
                            '\t>')

        if choice == '1':
            self._remove_payout_by_index()
        elif choice == '2':
            self._remove_payout_by_name()
        self.save()

    '''
    Фильтрует выплаты по категории.
    '''
    def filter_by_category(self) -> None:
        print('\nФильтрация выплат')
        category: str = input('>').lower()
        filtered_payouts: list[Payout] = list(filter(lambda payout: category in payout.get_category().lower(), self.__payouts))
        payouts = PayoutList(filtered_payouts)
        PayoutList.show_payouts(payouts)

    '''
    Возвращает суммарные затраты со всех выплат.
    '''
    def get_total_amount(self) -> Decimal:
        return sum(payout.get_amount() for payout in self.__payouts)
