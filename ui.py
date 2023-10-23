from logger import input_data, print_data, delete_data, put_data
def interface():
    print("Добрый день! Это чат-бот помощник.\n"
              "Что вы хотите сделать\n"
              "1 - Записать данные\n"
              "2 - Вывести данные\n"
              "3 - Удалить данные\n"
              "4 - Изменить данные")
    command = int(input("Ваш выбор: "))

    while command < 1 or command > 4:
        command = int(input("Ошибка! Ваш выбор: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
    elif command == 4:
        put_data()        

      
