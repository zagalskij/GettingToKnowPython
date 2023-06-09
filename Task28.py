# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 
def sum(a = None, b = None):
    if a is None:
        if a > b:
            a, b = a, b
        else:
            a, b = b, a
    if b == 0:
        return a
    return sum(a+1,b-1)


a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print(sum(a, b))