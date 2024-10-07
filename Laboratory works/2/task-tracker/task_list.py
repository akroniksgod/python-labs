from __future__ import annotations
from task import Task
import json

'''
Название файла, в котором храним список задач.
'''
json_name: str = 'tasks.json'

"""
Список задач.
"""
class TaskList:
    """
    Список задач.
    """
    _tasks: list[Task]

    '''
    Инициализирует список задач.
    '''
    def __init__(self, tasks: list[Task] = ()) -> None:
        self._tasks = tasks

    '''
    Возвращает строковое представление списка задач.
    '''
    def __str__(self) -> str:
        tasks: str = ''
        task_position: int = 1
        for task in self._tasks:
            tasks += f'\t{task_position} {task.__str__()};\n'
            task_position += 1
        return tasks

    '''
    Выводит список задач в консоль.
    '''
    def show(self) -> None:
        print('Задачи:')
        print(self.__str__())

    '''
    Показать список переданный задач в консоли.
    '''
    @staticmethod
    def show_tasks(tasks: TaskList) -> None:
        print('Задачи:')
        print(tasks.__str__())

    '''
    Возвращает список объектов.
    '''
    def _to_dict_list(self) -> list[dict]:
        return [task.to_dict() for task in self._tasks]

    '''
    Сохраняет список задач в json.
    '''
    def save(self) -> None:
        with open(json_name, 'w', encoding='utf-8') as f:
            json.dump(self._to_dict_list(), f, indent=4)
            print('Изменения сохранены!\n')

    '''
    Возвращает список задач.
    '''
    @staticmethod
    def get_saved_tasks(file_name: str) -> list[Task]:
        with open(file_name) as json_data:
            task_dict_list: list[dict] = json.load(json_data)
            return list(map(lambda task: Task.from_dict(task), task_dict_list))

    '''
    Добавляет задачу в список задач.
    '''
    def append(self, task: Task) -> None:
        self._tasks.append(task)

    '''
    Добавляет задачу в список задач.
    '''
    def add(self) -> None:
        print('\nСоздание задачи')
        name: str = input('\tНазвание: ')
        category: str = input('\tКатегория: ')
        description: str = input('\tОписание: ')
        checked: bool = False
        new_task = Task(name, description, category, checked)
        self.append(new_task)
        self.save()

    '''
    Редактирует задачу в список задач.
    '''
    def change(self) -> None:
        print('\nРедактирование задачи')
        position: str = input('\tВведите номер задачи: ')
        index: int = int(position) - 1
        if index < 0 or index >= len(self._tasks):
            print('Не удалось внести изменения!\n')
            return
        task: Task = self._tasks[index]
        print(f'\t{task}')
        choice: str = input('\t1. Изменить название;\n'
                            '\t2. Изменить описание;\n'
                            '\t3. Изменить категорию.\n'
                            '\t>')
        new_value: str = input('\tНовое значение: ')
        options: dict = {
            '1': task.set_name,
            '2': task.set_description,
            '3': task.set_category,
        }
        options[choice](new_value)
        self.save()

    '''
    Удаляет задачу из списка задач по названию.
    '''
    def _remove_task_by_name(self) -> None:
        name: str = input('\n\tНазвание: ').lower()
        self._tasks = filter(lambda x: str(x.name).lower() == name, self._tasks)

    '''
    Удаляет задачу из списка задач по индексу.
    '''
    def _remove_task_by_index(self) -> None:
        position: str = input('\n\tНомер: ')
        index: int = int(position) - 1
        self._tasks.pop(index)

    '''
    Удаляет задачу из списка задач.
    '''
    def remove(self) -> None:
        print('\nУдаление задачи')
        choice: str = input('\t1. Удалить по номеру;\n'
                            '\t2. Удалить по названию.\n'
                            '\t>')

        if choice == '1':
            self._remove_task_by_index()
        elif choice == '2':
            self._remove_task_by_name()
        self.save()

    '''
    Отмечает задачу из списка задач по названию.
    '''
    def _change_checked_by_task_name(self) -> None:
        name: str = input('\n\tНазвание: ').lower()
        filtered_tasks: list[Task] = filter(lambda task: task.get_name().lower() == name, self._tasks)
        selected_task: Task = filtered_tasks[0]
        selected_task.set_checked(not selected_task.get_checked())

    '''
    Отмечает задачу из списка задач по индексу.
    '''
    def _change_checked_by_task_index(self) -> None:
        position: str = input('\n\tНомер: ')
        index: int = int(position) - 1
        task: Task = self._tasks[index]
        task.set_checked(not task.get_checked())

    '''
    Отмечает задачу из списка задач.
    '''
    def change_checked(self) -> None:
        print('\nОтменить задачу')
        choice: str = input('\t1. Отменить по номеру;\n'
                            '\t2. Отменить по названию.\n'
                            '\t>')
        if choice == '1':
            self._change_checked_by_task_index()
        elif choice == '2':
            self._change_checked_by_task_name()
        self.save()

    '''
    Фильтрует задачи по категории.
    '''
    def filter_by_category(self) -> None:
        print('\nФильтрация задач')
        category: str = input('>').lower()
        filtered_tasks: list[Task] = filter(lambda task: category in task.get_category().lower(), self._tasks)
        tasks = TaskList(filtered_tasks)
        TaskList.show_tasks(tasks)

    '''
    Фильтрация по названию задачи.
    '''
    def filter_by_name(self) -> None:
        print('\nПоиск по задачам')
        name: str = input('>').lower()
        filtered_tasks: list[Task] = filter(lambda task: name in task.get_name().lower(), self._tasks)
        tasks = TaskList(filtered_tasks)
        TaskList.show_tasks(tasks)
