from math import sqrt
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
def CheckNatural(number, div=2):
    if div > number // sqrt(number)+1 or number == 2:
        return 'yes'
    if (number % div or number <= 1) == 0:
        return 'no'
    return CheckNatural(number,div+1)


number = int(input('Input: '))
print(f'Output: {CheckNatural(number)}')
