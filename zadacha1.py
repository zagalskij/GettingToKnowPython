# import random
# a = int(input("Enter the number of elements in the tuple: "))
# b = tuple(random.randint(0,10) for _ in range(a))
# print(*b)
# b=list(b)
# indexToReplace = int(input("Enter the index to replace: "))
# b[indexToReplace] = random.randint(0,10)
# b = tuple(b)
# print(*b)
import random


def change_element(numbers, index):
    return tuple(b[:indexToReplace] + (random.randint(0, 10),) + b[indexToReplace+1:])


a = int(input("Enter the number of elements in the tuple: "))
b = tuple(random.randint(0, 100) for _ in range(a))
print(*b)
indexToReplace = int(input("Enter the index to replace: "))
print(*change_element(b, indexToReplace))
