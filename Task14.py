# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
n = int(input("Enter n: "))
print(f"{n} ->", end=' ')
x = 0
counter = 0
while 2 ** counter <= n:
    print(2 ** counter, end=' ')
    counter+=1
