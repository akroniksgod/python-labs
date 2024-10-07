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
    '''
    Список задач.
    '''
    _tasks: list[Task]

    '''
    Инициализирует список задач.
    '''
    def __init__(self, tasks: list[Task] = ()):
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
    Возвращает список объектов.
    '''
    def _to_dist_list(self) -> list[dict]:
        return [task.to_dict() for task in self._tasks]

    '''
    Сохраняет список задач в json.
    '''
    def save(self) -> None:
        with open(json_name, 'w', encoding='utf-8') as f:
            json.dump(self._to_dist_list(), f, indent=4)
            print('Изменения сохранены!\n')

    '''
    Возвращает список задач.
    '''
    @staticmethod
    def get_saved_tasks(file_name: str) -> list[Task]:
        with open(file_name) as json_data:
            task_dict_list = json.load(json_data)
            return list(map(lambda task: Task.from_dict(task), task_dict_list))

    '''
    Добавляет задачу в список задач.
    '''
    def append(self, task: Task):
        self._tasks.append(task)

    '''
    Добавляет задачу в список задач.
    '''
    def add(self) -> None:
        print('\nСоздание задачи')
        name = input('\tНазвание: ')
        category = input('\tКатегория: ')
        description = input('\tОписание: ')
        checked = False
        new_task = Task(name, description, category, checked)
        self.append(new_task)
        self.save()

    '''
    Редактирует задачу в список задач.
    '''
    def change(self):
        print('\nРедактирование задачи')
        position = input('\tВведите номер задачи: ')
        task = self._tasks[int(position) - 1]

        choice = input('\t1. Изменить название;\n'
              '\t2. Изменить описание;\n'
              '\t3. Изменить категорию.\n'
              '\t>')
        new_value = input('\tНовое значение: ')
        options = {
            '1': task.set_name,
            '2': task.set_description,
            '3': task.set_category,
        }
        options[choice](new_value)
        self.save()

    '''
    Удаляет задачу из списка задач по названию.
    '''
    def _remove_by_task_name(self) -> None:
        name = input('\n\tНазвание: ').lower()
        self._tasks = filter(lambda x: str(x.name).lower() == name, self._tasks)

    '''
    Удаляет задачу из списка задач по индексу.
    '''
    def _remove_by_task_index(self) -> None:
        index = int(input('\n\tНомер: ')) - 1
        self._tasks.pop(index)

    '''
    Удаляет задачу из списка задач.
    '''
    def remove(self) -> None:
        print('\nУдаление задачи')
        choice = input('\t1. Удалить по номеру;\n'
                       '\t2. Удалить по названию.\n'
                       '\t>')

        if choice == '1':
            self._remove_by_task_index()
        elif choice == '2':
            self._remove_by_task_name()
        self.save()

    '''
    Отмечает задачу из списка задач по названию.
    '''
    def _change_checked_by_task_name(self) -> None:
        name = input('\n\tНазвание: ').lower()
        task = filter(lambda x: str(x.name).lower() == name, self._tasks)[0]
        task.set_checked(not task.get_checked())

    '''
    Отмечает задачу из списка задач по индексу.
    '''
    def _change_checked_by_task_index(self) -> None:
        index = int(input('\n\tНомер: ')) - 1
        task = self._tasks[index]
        task.set_checked(not task.get_checked())

    '''
    Отмечает задачу из списка задач.
    '''
    def change_checked(self) -> None:
        print('\nОтменить задачу')
        choice = input('\t1. Отменить по номеру;\n'
                       '\t2. Отменить по названию.\n'
                       '\t>')
        if choice == '1':
            self._change_checked_by_task_index()
        elif choice == '2':
            self._change_checked_by_task_name()
        self.save()
