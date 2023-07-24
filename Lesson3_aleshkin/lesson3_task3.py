"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

def my_func(a1, a2, a3):
    """
    if a1 >= a3 and a2 >= a3:
        return a1 + a2
    elif a1 >= a2 and a3 >= a2:
        return a1 + a3
    else:
        return a2 + a3
    """
    result = []
    args = [a1, a2, a3]
    max1 = max(args)
    result.append(max1)
    args.remove(max1)
    max2 = max(args)
    result.append(max2)
    result = sum(result)
    return result

print(f'Сумма: {my_func(int(input("1ый аргумент: ")), int(input("2ой аргумент: ")), int(input("3ий аргумент: ")))}')