# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны N 
# целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
n = int(input("Enter the number of elements in the array: "))
array = []
for i in range(n):
    array.append(int(input(f"Enter the {i} element array: ")))
print(*array)
x = int(input('Enter the desired number: '))
b=[abs(array[i]-x) for i in range(len(array))]
print(f"-> {array[b.index(min(b))]}")