def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    stack = []  # используем список как стек
    for char in brackets_row:
        if char == "(":
            stack.append(char)  # добавляем открывающую скобку
        elif char == ")":
            if not stack:  # если стек пустой, закрывающая скобка не имеет пары
                return False
            stack.pop()  # извлекаем последнюю открывающую скобку
    return len(stack) == 0  # если стек пуст в конце, все скобки корректны


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
