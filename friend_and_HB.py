SEARCH = 1
NEW_HB = 2
CHANGE = 3
DELETE = 4
EXIT = 5

def main():
        birthdays = {}
        choice = 0
        while choice != EXIT:
                choice = get_menu_choice()

                if choice == SEARCH:
                        search(birthdays)
                elif choice == NEW_HB:
                        new_hb(birthdays)
                elif choice == CHANGE:
                        change(birthdays)
                elif choice == DELETE:
                        delete(birthdays)

def get_menu_choice():
        print()
        print('Друзья и их дни рождения')
        print('------------------------')
        print('1. Найти день рождение')
        print('2. Добавить новое день рождение')
        print('3. Изменить день рождение')
        print('4. Удалить день рождение')
        print('5. Выход из программы')
        print()

        choice = int(input('Введите выбранный пункт: '))
        while choice > EXIT or choice < SEARCH:
                choice = int(input('Введите выбранный пункт: '))
        return choice

def search(birthdays):
        name = input('Введите имя: ')

        print(birthdays.get(name, 'Не найдено'))

def new_hb(birthdays):
        name = input('Введите имя: ')
        day = input('Введите день рождение: ')

        if name not in birthdays:
                birthdays[name] = day
        else:
                print('Эта запись уже существует')

def change(birthdays):
        name = input('Введите имя: ')

        if name in birthdays:
                day = input('Введите день рождение: ')

                birthdays[name] = day
        else:
                print('Это имя не найдено')

def delete(birthdays):
        name = input('Введите имя: ')

        if name in birthdays:
                del birthdays[name]
        else:
                print('Это имя не найдено')
main()