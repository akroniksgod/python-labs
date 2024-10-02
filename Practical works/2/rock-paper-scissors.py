import random


"""
Камень.
"""
ROCK: str = 'камень'


"""
Бумага.
"""
PAPER: str = 'бумага'


"""
Ножницы.
"""
SCISSORS: str = 'ножницы'


"""
Доступные пользователю выборы.
"""
CHOICES_MAP: dict = {
    '1': ROCK,
    '2': PAPER,
    '3': SCISSORS,
}


"""
Количество побед для завершения игры.
"""
END_GAME_WIN_COUNT: int = 5


"""
Возвращает выбор игрока.
"""
def get_user_choice() -> ROCK or PAPER or SCISSORS:
    is_correct_input: bool = False
    user_input: str = ''
    while not is_correct_input:
        user_input = input('Выберите (1 - камень, 2 - бумага, 3 - ножницы): ')
        contains_one_symbol: bool = len(user_input) == 1
        is_correct_input = contains_one_symbol and user_input.isdigit() and 1 <= int(user_input) <= 3

    return CHOICES_MAP[user_input]


"""
Основная программа выполнения игры.
"""
def rock_paper_scissors() -> None:
    is_running: bool = True
    opponent_win_count: int = 0
    user_win_count: int = 0
    while is_running:
        opponent_choice: ROCK or PAPER or SCISSORS = CHOICES_MAP[str(random.randint(1, 3))]
        user_choice: ROCK or PAPER or SCISSORS = get_user_choice()

        user_picked_rock: bool = user_choice == ROCK
        user_picked_paper: bool = user_choice == PAPER
        user_picked_scissors: bool = user_choice == SCISSORS

        opponent_picked_rock: bool = opponent_choice == ROCK
        opponent_picked_paper: bool = opponent_choice == PAPER
        opponent_picked_scissors: bool = opponent_choice == SCISSORS

        is_user_successful_choice: bool = (user_picked_rock and opponent_picked_scissors
                                or user_picked_paper and opponent_picked_rock
                                or user_picked_scissors and opponent_picked_paper)

        is_tie_choice: bool = user_choice == opponent_choice

        user_win_count = user_win_count + 1 if is_user_successful_choice else user_win_count
        opponent_win_count = opponent_win_count + 1 if not is_user_successful_choice and not is_tie_choice else opponent_win_count

        print(f'Вы выбрали `{user_choice}`')
        print(f'Соперник выбрал `{opponent_choice}`')
        print(f'{'Победа' if is_user_successful_choice else 'Ничья' if is_tie_choice else 'Поражение'}! Счёт: {user_win_count} - {opponent_win_count}\n')

        is_running = not (user_win_count == END_GAME_WIN_COUNT or opponent_win_count == END_GAME_WIN_COUNT)

    print(f'Игра окончена!\nПобедителем стал{'и Вы' if user_win_count > opponent_win_count else ' опонент'}!')


if __name__ == '__main__':
    rock_paper_scissors()
