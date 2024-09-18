
"""
Возвращает делители переданного числа.
"""
def get_divisors(n: int) -> list:
    if n <= 0:
        return []

    divisors: list = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors


"""
Является ли число простым.
Используем улучшенный наивный метод.
"""
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    n = 3331
    print(f'Делители числа {n} => {get_divisors(n)}')
    n <= 100_000 and print(f'Число {n} {'не ' if not is_prime(n) else ''}является простым')
