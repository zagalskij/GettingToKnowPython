import random
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
def MaxOnMin(evaluations):
    old_value = max(evaluations)
    for i in range(numberOfRatings):
        if evaluations[i] == old_value:
            evaluations[i] = min(evaluations)
    return evaluations
numberOfRatings = int(input('Enter the number of ratings: '))
evaluations = [random.randint(1, 5) for _ in range(numberOfRatings)]
print(f'Input: {numberOfRatings} ->' , *evaluations)
correctedEstimates = MaxOnMin(evaluations)
print("Output: ", *correctedEstimates)
