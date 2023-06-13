import time
# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
def fillArray(firstElement,difference, quantity):
    array = []
    quantity = (firstElement + (quantity - 1) * difference) + 1
    for i in range(firstElement, quantity, difference):
        array.append(i)
    return array


firstElement = int(input('Enter the first element: '))
difference = int(input('Enter the difference: '))
quantity = int(input('Enter the quantity: '))
print(fillArray(firstElement, difference, quantity))