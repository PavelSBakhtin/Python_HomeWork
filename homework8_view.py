# Основное меню для общения с пользователем
def show_menu() -> int:
    print("\n" + " " * 9 + "Corporate directory") # корпоративный справочник
    print("=" * 37) # строка разделитель
    print("1. Find an employee") # Найти сотрудника
    print("2. Find a fired employee") # Найти уволенного сотрудника
    print("3. Selection of employees by position") # выборка по должности
    print("4. Selection of employees by salary") # выборка по зарплате
    print("5. Add employee") # добавление сотрудника
    print("6. Delete employee") # удаление сотрудника
    print("7. Update employee details") # обновление данных сотрудника
    print("8. Export data in format .json") # экспорт в json
    print("9. Export data in format .txt") # экспорт в txt
    print("0. Finish work") # завершить работу
    print("=" * 37) # строка разделитель
    item = int(input("Select a menu item: ")) # выбрать действие
    while item < 0 or item > 9:
        print("Input error") # ошибка ввода
        item = int(input("Select a menu item: "))
    else:
        return item
