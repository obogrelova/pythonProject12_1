def remainder(a, b):
    if b == 0:
        raise ValueError('Деление на ноль невозможно')
    return a % b