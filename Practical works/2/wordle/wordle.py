import csv
import random


"""
Нужно ли отобразить в консоли загаданное число.
"""
SHOW_GUESSED_WORD: bool = True

"""
Название файла со словами
"""
WORDS_FILE_NAME: str = 'five_letter_words.csv'


"""
Возвращает случайное слово из файла.
"""
def get_random_word() -> str:
    word: str = ''
    with open(WORDS_FILE_NAME, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        random_row = random.choice(rows)
        word = random_row[0]
        SHOW_GUESSED_WORD and print(f"Случайно выбранное слово: {word}")
    return word


"""
Содержит ли цифры в слове.
"""
def has_digits(word: str) -> bool:
    digits: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return any(word.count(str(digit)) > 0 for digit in digits)


"""
Содержит ли латинские буквы в слове.
"""
def has_latin_letters(word: str) -> bool:
    letters: str = "qwertyuiopasdfghjklzxcvbnm"
    return any(word.count(letter) for letter in letters)


"""
Возвращает загаданное пользователем число
"""
def get_user_guess(word_size: int) -> str:
    is_fine: bool = False
    user_guess: str = ''
    while not is_fine:
        user_guess = input('Введите слово: ')
        is_correct_len: bool = len(user_guess) == word_size
        is_fine = is_correct_len and not has_digits(user_guess) and not has_latin_letters(user_guess)

    return user_guess.lower()


"""
Проверка слова пользователя.
"""
def check_user_guess(user_word: str, guessed_word: str, attempt_count: int) -> bool:
    buffer: str = ''
    word_length = len(user_word)
    guessed_letters_count: int = 0
    for i in range(word_length):
        is_same_letter: bool = guessed_word[i] == user_word[i]
        has_letter: bool = user_word[i] in guessed_word
        if is_same_letter:
            buffer += f'[{guessed_word[i]}]'
            guessed_letters_count += 1
        elif has_letter:
            buffer += f'({guessed_word[i]})'
        else:
            buffer += user_word[i]

    print(f'Попытка №{attempt_count}, проверка слова: {buffer}')

    return word_length == guessed_letters_count


"""
Основная программа выполнения игры.
"""
def wordle():
    word: str = get_random_word()
    word_length: int = len(word)
    max_attempts: int = 6
    attempt_count: int = 1
    is_running: bool = True
    has_attempts: bool = False
    while is_running:
        user_word: str = get_user_guess(word_length)
        is_word_guessed = check_user_guess(user_word, word, attempt_count)
        attempt_count += 1
        has_attempts = attempt_count <= max_attempts
        is_running = not is_word_guessed and has_attempts

    print(f'Cлово {'не' if not has_attempts else ''} угадано!')


if __name__ == '__main__':
    wordle()
