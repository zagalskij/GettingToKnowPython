import time
# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
def fillArray(firstElement,difference, quantity):
    array = []
    for i in range(quantity):
        array.append(firstElement + i * difference)
    return array


firstElement = int(input('Enter the first element: '))
difference = int(input('Enter the difference: '))
quantity = int(input('Enter the quantity: '))
print(fillArray(firstElement, difference, quantity))