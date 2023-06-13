from random import randint
# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
def fillArray():
    array = [randint(0,10) for _ in range(randint(1,10))]
    return array

def minMax(minValue, maxValue, array):
    arrayIndex = []
    for index, value in enumerate(array):
        if value >= minValue and value <=maxValue:
            arrayIndex.append(index)
    return array


minValue = int(input('Enter the minimum value: '))
maxValue = int(input('Enter the maximal value: '))
array = fillArray()
print(array)
minMax(minValue, maxValue, array)
