import random

list = [random.randint(1, 20) for _ in range(10)]
uniqueList = set(list)
print(f'{list} -> {uniqueList}')
print(f'Удалено элементов: {len(list) - len(uniqueList)}')

