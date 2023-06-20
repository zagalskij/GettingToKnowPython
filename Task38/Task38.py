# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
def show_all_records():
     with open('guide.txt', encoding='utf-8') as f:
        data = f.readlines()
        data = list(map(str.strip, data))
        print(*data, sep="\n")
        

def case_container():
    print(f"Select an option:\n1 - Person's code\n" + \
            '2 - Last name\n' + \
            '3 - Name\n' + \
            '4 - Middle name\n' + \
            '5 - Contact')
    number = int(input())
    if number == 1:
            search = input("enter the person's code: ")
    if number == 2:
            search = input("enter the last name: ")
    if number == 3:
            search = input("enter the name: ")
    if number == 4:
            search = input("enter the middle name: ")
    if number == 5:
            search = input("enter the contact: ")
    return number, search

def search_record(index_search, search: str):
    array_search = []
    flag = True
    with open("guide.txt", encoding='utf-8') as f:
        data = f.readlines()
        for i in data: 
            if  search.lower() in i.split(' ')[index_search-1].lower(): 
                array_search.append(i)
                flag = False
        if flag:
            print("Record not found")
        return array_search       

def add_contact(id, last_name, name, middle_name, number):
    with open('guide.txt','a', encoding='utf-8') as data:
        data.write('\n')
        data.write(f'{id} {last_name} {name} {middle_name} {number}')


def update(code_change: str, number, search):
    with open('guide.txt', encoding='utf-8') as f:
        data = f.readlines()
        for count, value in enumerate(data): 
            if  code_change in value.split(' ')[0]:
                data[count] = value.replace(value[int(number-1)],search)
    with open('guide.txt', 'w', encoding='utf-8') as file:
         file.writelines(data)


def delete(code_change):
    with open('D:\GIT\GettingToKnowPython\Task49\guide.txt', encoding='utf-8') as f:
        data = f.readlines()
        for count, value in enumerate(data): 
            if  code_change in value.split(' ')[0]:
                data[count] = ''
    with open('guide.txt', 'w', encoding='utf-8') as file:
         file.writelines(data)


def main():
    print(f'Select an action:\n1 - Show Directory\n' + \
    '2 - Find a contact\n' + \
    '3 - Add a contact\n' + \
    '4 - Change a contact\n' + \
    '5 - Delete a contact')
    select = int(input())
    if select == 1:
        show_all_records()
    elif select == 2:
        number, search = case_container()
        for i in search_record(number, search):
            print(i, end='')
    elif select == 3:
        id = tuple(input("Enter the person's code:"))
        last_name = input('Enter the full name: ')
        name = input('Enter the name: ')
        middle_name = input('Enter the middle name: ')
        number = input("Enter the number of phone: ")
        add_contact(*id, last_name, name, middle_name, number)
    elif select == 4:
        code_change = input("Enter the person's code: ")
        number, search = case_container()
        update(code_change, number, search)
    elif select == 5:
        code_change = input("Enter the person's code: ")
        delete(code_change)

main()