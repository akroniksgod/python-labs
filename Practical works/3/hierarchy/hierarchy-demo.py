from part_time_student import PartTimeStudent
from student import Student
from pupil import Pupil
from person import Person

"""
Выводит данные по человеку (базовый класс).
"""
def print_person() -> None:
    person = Person('Кирилл', 'Давыдов', 35, True)
    print(f'{person}\n')
    print(f'{repr(person)}\n')


"""
Выводит данные по школьнику (наследуется от человека).
"""
def print_pupil() -> None:
    pupil = Pupil('Петр', 'Воронцов', 13, True, '№25', 7)
    print(f'{pupil}\n')
    print(f'{repr(pupil)}\n')


"""
Выводит данные по студенту (наследуется от школьника).
"""
def print_student() -> None:
    student = Student('Игорь', 'Тортов', 25, True, 'ПНИПУ', 4, 'АСУ8-13-1м', 'АСУ')
    print(f'{student}\n')
    print(f'{repr(student)}\n')


"""
Выводит данные по студенту заочнику (наследуется от студента).
"""
def print_part_time_student() -> None:
    part_time_student = PartTimeStudent('Сергей', 'Туф', 25, True, 'ПНИПУ', 4, 'АСУ8-13-1мз', 'АСУ', 'ЭТФ-4202-199')
    print(f'{part_time_student}\n')
    print(f'{repr(part_time_student)}\n')


if __name__ == '__main__':
    print_person()
    print_pupil()
    print_student()
    print_part_time_student()
