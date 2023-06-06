# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
theFirstSet = int(input('Enter the first set: '))
theSecondSet = int(input('Enter the second set: '))
theFirstSet = [int(input()) for _ in range(theFirstSet)]
theSecondSet = [int(input()) for _ in range(theSecondSet)]
theFirstSet = set(theFirstSet)
theSecondSet = set(theSecondSet)
print(*theFirstSet.intersection(theSecondSet))
