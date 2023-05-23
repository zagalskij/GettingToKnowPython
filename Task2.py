# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Enter a number: "))
theThirdNumber = number % 10
theSecondNumber = number // 10 % 10
theFirstNumber = number // 100
print(f"{number} -> {theFirstNumber +  theSecondNumber + theThirdNumber} \
({theFirstNumber} + {theSecondNumber} + {theThirdNumber})")
