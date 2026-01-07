from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return []

        # Находим максимальный элемент, чтобы определить размер вспомогательного массива
    max_value = max(container)

    # Создаем вспомогательный массив counts для подсчета
    counts = [0] * (max_value + 1)

    # Подсчитываем количество каждого элемента
    for num in container:
        counts[num] += 1

    # Восстанавливаем отсортированный массив
    sorted_arr: List[int] = []
    for value, count in enumerate(counts):
        sorted_arr.extend([value] * count)  # добавляем value count раз

    return sorted_arr
