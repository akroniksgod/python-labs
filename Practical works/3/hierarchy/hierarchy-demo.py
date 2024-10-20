from part_time_student import PartTimeStudent
from student import Student
from pupil import Pupil
from person import Person

"""
Выводит данные по человеку (базовый класс).
"""
def print_person() -> None:
    person = Person('Кирилл', 'Давыдов', 35, True)
    another_person = Person('Жорик', 'Псковский', 23, True)
    check_overloaded_methods(person, another_person)


"""
Выводит данные по школьнику (наследуется от человека).
"""
def print_pupil() -> None:
    pupil = Pupil('Петр', 'Воронцов', 13, True, '№25', 7)
    another_pupil = Pupil('Лёша', 'Лупин', 15, True, '№25', 9)
    check_overloaded_methods(pupil, another_pupil)


"""
Выводит данные по студенту (наследуется от школьника).
"""
def print_student() -> None:
    student = Student('Игорь', 'Тортов', 35, True, 'ПНИПУ', 4, 'АСУ8-13-1м', 'АСУ')
    another_student = Student('Олег', 'Попов', 25, True, 'ПНИПУ', 4, 'АСУ2-13-1м', 'АСУ')
    check_overloaded_methods(student, another_student)


"""
Выводит данные по студенту заочнику (наследуется от студента).
"""
def print_part_time_student() -> None:
    part_time_student = PartTimeStudent('Сергей', 'Туф', 25, True, 'ПНИПУ', 4, 'АСУ8-13-1мз', 'АСУ', 'ЭТФ-4202-199')
    another_part_time_student = PartTimeStudent('Сергей', 'Туф', 25, True, 'ПНИПУ', 4, 'АСУ8-13-1мз', 'АСУ', 'ЭТФ-4202-199')
    check_overloaded_methods(part_time_student, another_part_time_student)


"""
Выводит результат проверки перегруженных методов.
"""
def check_overloaded_methods(person, another_person) -> None:
    print(f'str: {person}\n')
    print(f'repr: {repr(person)}\n')
    print(f'==: {person == another_person}')
    print(f'!=: {person != person}')
    print(f'>: {person > another_person}')
    print(f'>=: {person >= another_person}')
    print(f'<=: {person <= another_person}')
    print(f'<: {person < another_person}\n')


if __name__ == '__main__':
    print_person()
    print_pupil()
    print_student()
    print_part_time_student()
