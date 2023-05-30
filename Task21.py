# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

dictionary = {}
length = int(input("Введите длину словаря:"))
for element in range(0,length):
  dictionary[input()] = input()
print(type(dictionary))
for key, value in dictionary.items():
    print(key, value)
u_value = set(value for dic in dictionary for value in dic.values())
print("Unique Values: ",u_value)