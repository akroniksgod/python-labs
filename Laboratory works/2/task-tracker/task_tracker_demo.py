from task_list import TaskList, json_name
from task import Task
# import os
# import subprocess


'''
Очищает консоль.
'''
# def cls():
#     subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
#     subprocess.call('powershell -Command Clear-Host', shell=True)


'''
Генерирует список задач.
'''
def generate_tasks() -> list[Task]:
    task_list: list[Task] = []
    task_list.append(Task('Тест 1', '', '', False))
    task_list.append(Task('Тест 2', 'Тест 2', '', False))
    task_list.append(Task('Тест 3', 'Тест', '', False))
    return task_list


'''
Возвращает опции в меню.
'''
def get_menu_options() -> str:
    return (f'1. Создать задачу;\n'
            f'2. Изменить задачу;\n'
            f'3. Отметить задачу;\n'
            f'4. Удалить задачу;\n'
            f'5. Выгрузить задачи из json;\n'
            f'6. Фильтрация по категориям;\n'
            f'7. Поиск по названию;\n'
            f'8. Закрыть.\n'
            f'>')


if __name__ == '__main__':
    tasks: list[Task] = []
    try:
        tasks = TaskList.get_saved_tasks(json_name)
    except FileNotFoundError:
        tasks = generate_tasks()
    task_list = TaskList(tasks)

    def load_tasks() -> None:
        task_list.get_saved_tasks(json_name)

    is_running: bool = True

    def close() -> None:
        global is_running
        is_running = False

    menu_options = {
        '1': task_list.add,
        '2': task_list.change,
        '3': task_list.change_checked,
        '4': task_list.remove,
        '5': load_tasks,
        '6': task_list.filter_by_category,
        '7': task_list.filter_by_name,
        '8': close,
    }

    while is_running:
        # cls()
        task_list.show()
        choice = input(get_menu_options())
        menu_options[choice]()
