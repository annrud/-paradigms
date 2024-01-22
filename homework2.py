# На вход подается число n.
# Написать скрипт в любой парадигме,
# который выводит на экран таблицу умножения всех чисел от 1 до n.

# Выбрана процедурная парадигма, так как для каждого ввода числа n
# удобно вызвать функцию вывода таблицы умножения.
def get_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            result = i * j
            print(f'{i} * {j} = {result}')


if __name__ == "__main__":
    try:
        n = int(input("Введите число n: "))
        get_multiplication_table(n)
    except ValueError:
        print("Введено не корректное число.")
