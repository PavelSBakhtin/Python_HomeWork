import homework7_controller as con
import homework7_module as mod

def menu():
    while True:
        print('\nMENU:')
        print('1. Create phone book .txt')
        print('2. Create phone book .csv')
        print('3. Export to .txt')
        print('4. Export to .csv')
        n = input('Select item of menu: ')
        if n == 1:
            con.create_book(1)
        if n == 2:
            con.create_book(2)
        if n == 3:
            mod.export_txt()
        if n == 4:
            mod.export_csv()
        else:
            break
