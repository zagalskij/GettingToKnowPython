# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
def Degree(a, b):
    if b==0:
        return 1
    return a * Degree(a, b - 1)


a = int(input('Enter the number: '))
b = int(input('Enter the degree: '))
print(f'A = {a}; B = {b} -> {Degree(a, b)}')