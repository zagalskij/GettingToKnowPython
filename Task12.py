import math
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input("Enter the sum of the numbers: "))
p = int(input("Enter the product of the numbers: "))
a, b, c = 1, -s, p
discriminant = b * b -4 * a * c
if discriminant < 0.000001:
    x = int(-b / 2*a)
else:
    x = int((-b + math.sqrt(discriminant)) / (2*a))
y = s - x
print(f"{s} {p}-> {y} {x}")