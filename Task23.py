# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
count = int(input("Enter numer elements in array"))
array = []
countF = 0
for i in range(count):
    array.append(input())
print(f'Input: {array}')
for i in range(count-1):
    if array[i]<array[i+1]:
        countF+=1
print(countF)