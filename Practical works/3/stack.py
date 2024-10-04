from __future__ import annotations
from typing import TypeVar

"""
Шаблонный тип.
"""
T = TypeVar("T")


"""
Узел стека.
"""
class StackNode:
    """
    Значение узла.
    """
    __value: T

    """
    Указатель на прошлый элемент.
    """
    __prev_node: StackNode

    """
    Инициализация узла стека.
    """
    def __init__(self, value: T) -> None:
        self.__value = value
        self.__prev_node = None

    """
    Возвращает значение узла.
    """
    def get_value(self) -> T:
        return self.__value

    """
    Возвращает прошлый узел.
    """
    def get_prev_node(self) -> StackNode:
        return self.__prev_node

    """
    Сохраняет значение узла.
    """
    def set_value(self, value) -> None:
        self.__value = value

    """
    Сохраняет прошлый узел.
    """
    def set_prev_node(self, node) -> None:
        self.__prev_node = node

"""
Стек.
"""
class Stack:
    """
    Инициализация стека.
    """
    def __init__(self, value: T) -> None:
        self.__current_node = StackNode(value)
        self._count = 1

    """
    Показывает стек.
    """
    def show(self) -> None:
        print("Просмотр стека")
        count = self._count
        stack_copy = self.__current_node

        while count > 0:
            current_value = stack_copy.get_value()
            prev_node = stack_copy.get_prev_node()
            print(current_value)
            stack_copy = prev_node
            count -= 1
        print()

    """
    Сохраняет узел на вершине стека.
    """
    def push(self, value: T) -> None:
        self._count += 1
        new_node = StackNode(value)
        new_node.set_prev_node(self.__current_node)
        self.__current_node = new_node

    """
    Удаляет узел с вершины стека.
    """
    def pop(self) -> None:
        if self._count == 0:
            pass

        prev_node = self.__current_node.get_prev_node()
        self.__current_node.set_value(None)
        self.__current_node = prev_node
        self._count -= 1


if __name__ == '__main__':
    # Создание стека
    stk = Stack("Первый элемент")
    stk.show()

    # Проверка добавления элементов
    stk.push("Второй элемент")
    stk.push("Третий элемент")
    stk.push("Четвёртый элемент")
    stk.show()

    # Проверка удаления элементов
    stk.pop()
    stk.pop()
    stk.show()
