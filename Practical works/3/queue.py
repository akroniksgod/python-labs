from __future__ import annotations
from typing import TypeVar

"""
Шаблонный тип.
"""
T = TypeVar("T")


"""
Узел для очереди.
"""
class QueueNode:
    """
    Значение узла.
    """
    __value: T

    """
    Указатель на следующий элемент.
    """
    __next_node: QueueNode | None

    """
    Инициализация узла очереди.
    """
    def __init__(self, value: T) -> None:
        self.__value = value
        self.__next_node = None

    """
    Возвращает значение узла.
    """
    def get_value(self) -> T:
        return self.__value

    """
    Возвращает прошлый узел.
    """
    def get_next_node(self) -> QueueNode | None:
        return self.__next_node

    """
    Сохраняет значение узла.
    """
    def set_value(self, value: T) -> None:
        self.__value = value

    """
    Сохраняет прошлый узел.
    """
    def set_next_node(self, node: QueueNode | None) -> None:
        self.__next_node = node


"""
Очередь.
"""
class Queue:
    """
    Текущий узел очереди.
    """
    __current_node: QueueNode | None

    """
    Инициализация очереди.
    """
    def __init__(self, value: T) -> None:
        self.__current_node = QueueNode(value)

    """
    Добавление элемента в очередь.
    """
    def push(self, value: T) -> None:
        new_node = QueueNode(value)
        current = self.__current_node
        while current.get_next_node() is not None:
            current = current.get_next_node()
        current.set_next_node(new_node)

    """
    Показывает элементы очереди.
    """
    def show(self) -> None:
        print("Просмотр очереди")
        current = self.__current_node
        while current is not None:
            print(current.get_value())
            current = current.get_next_node()
        print()

    """
    Удаляет первый элемент очереди.
    """
    def pop(self) -> None:
        if self.__current_node is None:
            pass

        self.__current_node = self.__current_node.get_next_node()


if __name__ == '__main__':
    # Создание очереди
    queue = Queue("Первый элемент")
    queue.show()

    # Проверка добавления элементов
    queue.push("Второй элемент")
    queue.push("Третий элемент")
    queue.push("Четвёртый элемент")
    queue.show()

    # Проверка удаления элементов
    queue.pop()
    queue.pop()
    queue.show()
