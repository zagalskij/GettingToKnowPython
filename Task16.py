# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых 
# чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
n = int(input("Enter the number of elements in the array: "))
array = []
for i in range(n):
    array.append(int(input(f"Enter the {i} element array: ")))
print(*array)
x = int(input('Enter the desired number: '))
print(f'-> {array.count(x)}')