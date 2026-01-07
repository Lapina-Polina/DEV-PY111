from typing import Union, Tuple

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    target = max(graph.nodes)  # верхняя ступень
    # кратчайший путь по весам от земли (0) до верхней ступени
    return nx.shortest_path_length(graph, source=0, target=target, weight='weight')


def build_stairway_graph(costs: Tuple[int, ...]) -> nx.DiGraph:
    """
    Построить граф лестницы для автопроверки.

    :param costs: кортеж с стоимостью каждой ступени
    :return: граф NetworkX с вершинами и ребрами, по которому можно найти минимальную стоимость подъема
    """
    n = len(costs)  # количество ступеней
    G = nx.DiGraph()  # создаем направленный граф
    G.add_node(0)  # добавляем узел "земля"

    for i in range(n):
        G.add_node(i + 1)  # добавляем узел для каждой ступени
        # С земли можно пойти на первую или вторую ступеньку
        if i == 0:
            G.add_edge(0, 1, weight=costs[0])  # ход на первую ступень
            if n > 1:
                G.add_edge(0, 2, weight=costs[1])  # ход на вторую ступень (перепрыгнуть)
        # Обычные переходы с текущей ступени:
        # на следующую ступень
        if i + 1 <= n:
            G.add_edge(i + 1, i + 2, weight=costs[i + 1 - 1])
        # через одну ступень (перепрыгнуть)
        if i + 2 <= n:
            G.add_edge(i + 1, i + 3, weight=costs[i + 2 - 1])
    return G  # возвращаем готовый граф


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = build_stairway_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
