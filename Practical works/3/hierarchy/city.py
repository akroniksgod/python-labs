from __future__ import annotations
import random
from dataclasses import dataclass
from person import Person
from pupil import Pupil

"""
Модель город.
"""
@dataclass
class City:
    """
    Люди в городе.
    """
    _people: list

    """
    Вывод списка всех людей в городе.
    """
    def show(self, operator: str = '') -> None:
        len(operator) > 0 and print(operator)
        i: int = 1
        for current_person in self._people:
            print(f'{i}) {current_person}')
            i += 1
        print()

    """
    Перегрузка '+'.
    """
    def __add__(self, other: Person) -> None:
        if not isinstance(other, Person):
            pass
        self._people.append(other)

    """
    Перегрузка '+='.
    """
    def __iadd__(self, other: Person) -> City:
        if not isinstance(other, Person):
            pass
        self.__add__(other)
        return City(self._people)

    """
    Перегрузка '-'.
    """
    def __sub__(self, other) -> None:
        if not isinstance(other, Person):
            pass
        self._people.remove(other)

    """
    Перегрузка '-='.
    """
    def __isub__(self, other: Person) -> City:
        if not isinstance(other, Person):
            pass
        self.__sub__(other)
        return City(self._people)

    """
    Перегрузка '*'.
    Добавляет случайного человека нужное число раз.
    """
    def __mul__(self, other: int) -> None:
        if not isinstance(other, int):
            pass
        selected_person: Person = random.choice(self._people)
        for i in range(other):
            self.__add__(selected_person)

    """
    Перегрузка '*='.
    Увеличивает население города на нужное количество человек.
    """
    def __imul__(self, other: int) -> City:
        if not isinstance(other, int):
            pass
        selected_person: Person = random.choice(self._people)
        for i in range(other):
            self._people.append(selected_person)
        return City(self._people)

    """
    Перегрузка '/'.
    Сокращает население на нужное количество человек.
    """
    def __truediv__(self, other: int) -> None:
        person_count: int = len(self._people)
        if not isinstance(other, int) or person_count < other:
            pass
        i: int = 0
        person_index: int = person_count - 1
        while i < other:
            self._people.pop(person_index)
            person_index -= 1
            i += 1

    """
    Перегрузка '/='.
    Сокращает население на нужное количество человек.
    """
    def __itruediv__(self, other: int) -> City:
        if not isinstance(other, int):
            pass
        self.__truediv__(other)
        return City(self._people)

    """
    Перегрузка '//'.
    Сокращает население в нужное количество человек.
    """
    def __floordiv__(self, other: int) -> None:
        person_count: int = len(self._people)
        if not isinstance(other, int) or person_count < other:
            pass
        new_count = person_count // other
        new_people = []
        for i in range(new_count):
            new_people.append(self._people[i])

        self._people.clear()
        self._people = new_people

    """
    Перегрузка '//='.
    Сокращает население в нужное количество человек.
    """
    def __ifloordiv__(self, other: int) -> City:
        if not isinstance(other, int):
            pass
        self.__floordiv__(other)
        return City(self._people)

    """
    Перегрузка '**'.
    Сокращает население в нужное количество человек.
    """
    def __pow__(self, other: int) -> None:
        if not isinstance(other, int):
            pass
        for i in range(len(self._people) * other):
            self._people.append(random.choice(self._people))

    """
    Перегрузка '**='.
    Сокращает население в нужное количество человек.
    """
    def __ipow__(self, other: int) -> City:
        if not isinstance(other, int):
            pass
        self.__pow__(other)
        return City(self._people)


if __name__ == '__main__':
    # Создаём город
    city = City([])

    # Тестовые люди
    person = Person('Кирилл', 'Давыдов', 35, True)
    another_person = Person('Жорик', 'Псковский', 23, True)

    # Добавляем людей в город
    city + person
    city.show('+')
    city += another_person
    city.show('+=')

    # Добавляем школьников в город
    pupil = Pupil('Петр', 'Воронцов', 13, True, '№25', 7)
    another_pupil = Pupil('Лёша', 'Лупин', 15, True, '№25', 9)
    city + pupil
    city + another_pupil
    city.show('+')

    # Исключаем человека из города
    city - person
    city.show('-')

    # Исключаем школьника из города
    city -= pupil
    city.show('-=')

    # Увеличиваем город на 3 случайных людей
    city * 2
    city.show('*')

    # Увеличиваем город на 2 случайных людей
    city *= 4
    city.show('*=')

    # Сокращаем город на 2 случайных людей
    city / 2
    city.show('/')

    # Сокращаем город на 2 случайных людей
    city /= 2
    city.show('/=')

    # Сокращаем население города в 2 раза
    city // 2
    city.show('//')

    # Сокращаем население города в 2 раза
    city //= 2
    city.show('//=')

    # Умножает население в 2 раза
    city ** 2
    city.show('**')

    # Умножает население в 2 раза
    city **= 2
    city.show('**=')