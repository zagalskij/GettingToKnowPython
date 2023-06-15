from random import randint


def fillArray():
        array = [randint(1,10) for _ in range(randint(1,10))]
        return array


# def couple(array):
#         res = list()
#         for value in array:
#                 if value % 2 == 0:
#                         res.append((value, value**2))
#         return res


# array = fillArray()
# print(array)
# print(couple(array))


array = fillArray()
print(array)
res = list(filter(lambda x: x % 2 ==0, array))
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)