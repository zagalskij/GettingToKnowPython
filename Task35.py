# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
def CheckNatural(number):
    if number % 1 == 0 and number % number == 0:
        return 'yes'
    return 'no'
number = int(input('Enter thr number: '))
print(f'Input: {number}')
print(f'Output: {CheckNatural(number)}') 