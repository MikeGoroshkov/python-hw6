# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

def main():
    n = int(input("Ведите число: "))
    list_numbers = range(1, n+1)
    member = lambda x: (1+1/x)**x
    list_members = list(map(member, list_numbers))
    print(list_members)
    print(sum(list_members))
    

if __name__ == '__main__':
    main()