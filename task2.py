# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

def main():
    numbers = [1, 2, 3, 1, 3, 4, 5, 7, 5]
    print(list_unique_numbers(numbers))


def list_unique_numbers(numbers):
    return list(filter(lambda i: numbers.count(i) == 1, numbers))


if __name__ == '__main__':
    main()