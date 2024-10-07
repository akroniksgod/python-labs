from task_list import TaskList, json_name
from task import Task
# import os
# import subprocess


# def cls():
#     subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
#     subprocess.call('powershell -Command Clear-Host', shell=True)


def generate_tasks() -> list[Task]:
    task_list: list[Task] = []
    task_list.append(Task('Тест 1', '', '', False))
    task_list.append(Task('Тест 2', 'Тест 2', '', False))
    task_list.append(Task('Тест 3', 'Тест', '', False))
    return task_list


def get_menu_options() -> str:
    return (f'1. Создать задачу;\n'
            f'2. Изменить задачу;\n'
            f'3. Отметить задачу;\n'
            f'4. Удалить задачу;\n'
            f'5. Выгрузить задачи из json;\n'
            f'6. Закрыть.\n'
            f'>')


if __name__ == '__main__':
    tasks: list[Task] = TaskList.get_saved_tasks(json_name)
    task_list = TaskList(tasks)
    is_running: bool = True

    def close() -> None:
        global is_running
        is_running = False

    def load_tasks() -> None:
        task_list.get_saved_tasks(json_name)

    menu_options = {
        '1': task_list.add,
        '2': task_list.change,
        '3': task_list.change_checked,
        '4': task_list.remove,
        '5': load_tasks,
        '6': close,
    }

    while is_running:
        # cls()
        task_list.show()
        choice = input(get_menu_options())
        menu_options[choice]()
