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
     with open('guide.txt') as f:
        data = f.readlines()
        data = list(map(str.strip, data))
        print(*data, sep="\n")
        

def search_record(last_name: str):
    array_search_str = []
    flag = True
    with open("guide.txt") as f:
        data = f.readlines()
        for i in data: 
            if  last_name.lower() in i.split(' ')[1].lower(): 
                array_search_str.append(i)
                print(i)
                flag = False
        if flag:
            print("Record not found")
                

def add_contact(id, last_name, name, middle_name, number):
    with open('guide.txt','a') as data:
        data.write('\n')
        data.write(f'{id} {last_name} {name} {middle_name} {number}')


def update(code_change):
    search_record(code_change)



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
        search_last_name = input("enter the last name to search for: ")
        search_record(search_last_name)
    elif select == 3:
        id = tuple(input("Enter the person's code:"))
        last_name = input('Enter the full name: ')
        name = input('Enter the name: ')
        middle_name = input('Enter the middle name: ')
        number = input("Enter the number of phone: ")
        add_contact(*id, last_name, name, middle_name, number)
    elif select == 4:
        code_change = input('Enter the code of the person whose data you want to change: ')
        update(code_change)
    elif select == 5:

main()