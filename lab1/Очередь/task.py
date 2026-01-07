"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди — индекс 0
        Конец очереди — конец списка
        """
        self._data = []  # инициализация списка

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._data.append(elem)  # метод enqueue, O(1)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self._data:
            raise IndexError("Очередь пуста")
        return self._data.pop(0)  # O(n)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Индекс должен быть целым числом")

        if ind < 0 or ind >= len(self._data):
            raise IndexError("Индекс вне границ очереди")

        return self._data[ind]  # O(1)

    def clear(self) -> None:
        """ Очистка очереди. """
        self._data.clear()  # O(1)

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self._data)  # O(1)
