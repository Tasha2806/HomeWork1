from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор'))
    
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write( f'{name};{surname};{phone};{adress}\n\n')

def print_data():
    print('данные из файла1\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('данные из файла2\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(data_second)
    return data_first, data_second 


def change_line():
    

def put_data():
    print('Какой файл Вы хотите изменить?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ошибка! Введите данные.')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  
        print("Какую запись Вы хотите изменить?")
        number_line = int(input('Введите номер записи: '))
        number_line -= 1
        change_line(data_first, number_line, 1)
    else:
        print("Какую запись Вы хотите изменить?")
        number_line = int(input('Введите номер записи: '))
        number_line -= 1
        change_line(data_second, number_line, 2)


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ошибка! Введите данные.')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  
        print("Какую запись Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
       
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        
        data_first = data_first[:number_journal - 1] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
       
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  
          
def print_data():
    print("1файл")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="")
          
    print("2файл")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i !='\n':
                print(i, end="")
