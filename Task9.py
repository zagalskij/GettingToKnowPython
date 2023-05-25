# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 
n = int(input("Enter the factorial value"))
print(f"Input: {n}")
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(f"Output: {factorial}")