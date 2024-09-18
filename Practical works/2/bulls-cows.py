import random


"""
Нужно ли отобразить в консоли загаданное число.
"""
SHOW_GUESSED_NUMBER: bool = True


"""
Возвращает число со всеми случайными цифрами.
"""
def generate_unique_number(guess_size: int) -> int:
    buffer: str = ''

    for i in range(guess_size):
        should_go_next: bool = False
        while not should_go_next:
            digit: int = random.randint(1, 9)
            contains_digit: bool = str(digit) in buffer
            if not contains_digit:
                buffer += str(digit)
                should_go_next = True

    return int(buffer)


"""
Возвращает загаданное пользователем число
"""
def get_user_guess(guess_size: int) -> int:
    is_fine: bool = False
    user_guess: str = ''
    while not is_fine:
        user_guess = input('Введите число: ')
        is_correct_len: bool = len(user_guess) == guess_size
        is_fine = is_correct_len and user_guess.isdigit()

    return int(user_guess)


"""
Возвращает число коров.
"""
def get_cows_count(user_guess: str, guess: str):
    cows_count: int = 0
    index: int = 0
    for i in guess:
        is_cow: bool = i == user_guess[index]
        cows_count = cows_count + 1 if is_cow else cows_count
        index += 1

    return cows_count


"""
Возвращает число быков.
"""
def get_bulls_count(user_guess: str, guess: str):
    bulls_count: int = 0

    for i in range(len(user_guess)):
        has_digit: bool = user_guess[i] in guess
        is_same_position: bool = user_guess[i] == guess[i]
        bulls_count = bulls_count + 1 if has_digit and not is_same_position else bulls_count

    return bulls_count


"""
Проверяет попытку пользователя.
"""
def check_attempt(user_guess: str, guess: str, attempt_count: int) -> bool:
    cows_count: int = get_cows_count(user_guess, guess)
    bulls_count: int = get_bulls_count(user_guess, guess)
    print(f'Попытка {attempt_count};\nКоров: {cows_count}, быков: {bulls_count}')
    return not cows_count == len(user_guess)


"""
Основная программа выполнения игры.
"""
def bulls_cows(guess_size: int) -> None:
    is_running: bool = True
    guess: int = generate_unique_number(guess_size)
    attempt_count: int = 1
    SHOW_GUESSED_NUMBER and print(f'Загадано: {guess}')
    while is_running:
        user_guess: int = get_user_guess(guess_size)
        is_running = check_attempt(str(user_guess), str(guess), attempt_count)
        attempt_count += 1


if __name__ == '__main__':
    max_guess_size: int = 9
    default_guess_size: int = 4
    guess_size: int = 4

    bulls_cows(guess_size if guess_size <= max_guess_size else default_guess_size)
