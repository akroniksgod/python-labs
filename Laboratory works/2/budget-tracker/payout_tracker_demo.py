from decimal import Decimal
from payout_tracker import PayoutList, json_name
from payout import Payout


'''
Генерирует список выплат.
'''
def generate_payouts() -> list[Payout]:
    payout_list: list[Payout] = []
    payout_list.append(Payout('Выплата 1', Decimal(19150.6), 'test', ''))
    payout_list.append(Payout('Ноутбук', Decimal(97894.88949), 'test', ''))
    payout_list.append(Payout('Выплата 3', Decimal(4985.55), 'test', ''))
    payout_list.append(Payout('Хлеб', Decimal(50.126), 'groceries', ''))
    return payout_list


'''
Возвращает опции в меню.
'''
def get_menu_options() -> str:
    return (f'1. Создать выплату;\n'
            f'2. Изменить выплату;\n'
            f'3. Удалить выплату;\n'
            f'4. Выгрузить выплаты из json;\n'
            f'5. Фильтрация по категориям;\n'
            f'6. Закрыть.\n'
            f'>')


if __name__ == '__main__':
    payouts: list[Payout] = []
    try:
        payouts = PayoutList.get_saved_payouts(json_name)
    except FileNotFoundError:
        payouts = generate_payouts()

    payout_list = PayoutList(payouts)
    is_running: bool = True

    def close() -> None:
        global is_running
        is_running = False

    def load_payouts() -> None:
        payout_list.get_saved_payouts(json_name)

    menu_options: dict = {
        '1': payout_list.add,
        '2': payout_list.change,
        '3': payout_list.remove,
        '4': load_payouts,
        '5': payout_list.filter_by_category,
        '6': close,
    }

    while is_running:
        # cls()
        payout_list.show()
        choice: str = input(get_menu_options())
        menu_options[choice]()
