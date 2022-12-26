import csv
import json

def read_database():
    employees = []
    with open('homework8_database_a.csv', 'r', encoding = 'UTF-8-sig') as data:
        reader = csv.DictReader(data, delimiter = ",")
        for row in reader:
            employees.append(row)
    return employees

def read_deleted():
    employees = []
    with open('homework8_database_d.csv', 'r', encoding = 'UTF-8-sig') as data:
        reader = csv.DictReader(data, delimiter = ",")
        for row in reader:
            employees.append(row)
    return employees

def change_database(data, path = 'homework8_database_a.csv'):
     with open(path, 'w', encoding = 'UTF-8-sig') as new_data:
        fieldnames = ['id','surname','first_name','position','phone','salary']
        writer = csv.DictWriter(new_data, fieldnames = fieldnames, delimiter = ",", lineterminator = "\n")
        writer.writeheader()
        writer.writerows(data)
        print('=' * 30 + '\nDatabase changed')

def change_deleted(data_d, path = 'homework8_database_d.csv'):
     with open(path, 'w', encoding = 'UTF-8-sig') as new_data:
        fieldnames = ['id','surname','first_name','position','phone','salary']
        writer = csv.DictWriter(new_data, fieldnames = fieldnames, delimiter = ",", lineterminator = "\n")
        writer.writeheader()
        writer.writerows(data_d)
        print('=' * 30 + '\nDatabase changed')

def new_info(row):
    temp = dict()
    temp["id"] = int(row[0])
    temp["surname"] = row[1].title()
    temp["first_name"] = row[2].title()
    temp["position"] = row[3].title()
    temp["phone"] = row[4]
    temp["salary"] = int(row[5])
    return temp

def find_employee(data):
    print('\nEmployee search\n' + '=' * 72)
    employee = input('Enter the surname or first name of the employee: ')
    print('=' * 72)
    print('id surname name position phone salary')
    [print(*i) for i in map(dict.values,
                            filter(lambda x: x['surname'].lower() == employee.lower()
                                    or x['first_name'].lower() == employee.lower(), data))]

# find_employee(read_database())

def find_fired(data_d):
    print('\nEmployee search of fired\n' + '=' * 72)
    employee = input('Enter the surname or first name of the employee: ')
    print('=' * 72)
    print('id surname name position phone salary')
    [print(*i) for i in map(dict.values,
                            filter(lambda x: x['surname'].lower() == employee.lower()
                                    or x['first_name'].lower() == employee.lower(), data_d))]
    
# find_fired(read_deleted())

def select_position(data):
    print('\nSelection of employees by position\n' + '=' * 38)
    positions = [i for i in enumerate(sorted(set(map(lambda x: x['position'], data))), 1)]
    [print(*i) for i in positions]
    print('=' * 38)
    choice = positions[int(input('Select the position: ')) - 1][1]
    print(f'\n{choice}:')
    print('=' * 72)
    [print(*i) for i in map(dict.values, filter(lambda x: x['position'] == choice, data))]

# select_position(read_database())

def select_salary(data):
    print('\nSelection of employees by salary\n' + '=' * 38)
    min_salary = int(input("Enter the MIN of salary: "))
    max_salary = int(input("Enter the MAX of salary: "))
    print('=' * 72)
    [print(*i) for i in map(dict.values,
                            filter(lambda x: min_salary <= int(x.get('salary')) <= max_salary, data))]

# select_salary(read_database())

def add_employee(data, data_d):
    a = int(data[-1]['id'])
    all_id = []; k = 0
    while k < len(data_d):
        all_id.append(int(data_d[k]['id']))
        k += 1
    b = max(all_id)
    c = a if a > b else b
    print('\nAdding a new employee\n' + '=' * 30)
    params = [c + 1, input('Enter surname: '), input('Enter first name: '), input('Enter position: '),
                input('Enter phone: '), input('Enter salary: ')]
    info = [i for i in params]
    data.append(new_info(info))
    change_database(data)

add_employee(read_database(),read_deleted())

def del_employee(data, data_d):
    print('\nDismissal of an employee\n' + '=' * 30)
    empl_id = int(input('Enter employee ID: '))
    index = int(*map(data.index, filter(lambda x: int(x['id']) == empl_id, data)))
    params = [empl_id, data[index]['surname'], data[index]['first_name'], data[index]['position'],
                data[index]['phone'], data[index]['salary']]
    info = [i for i in params]
    data_d.append(new_info(info))
    change_deleted(data_d)
    print("Result: ", data[index]['surname'], data[index]['first_name'], data[index]['position'], "- successfully fired")
    data.pop(index)
    change_database(data)

# del_employee(read_database(), read_deleted())

def upd_employee(data):
    print("\nUpdating an employee's data\n" + '=' * 30)
    empl_id = int(input('Enter employee ID: '))
    index = int(*map(data.index, filter(lambda x: int(x['id']) == empl_id, data)))
    print(*data[index].values())
    print('1 - Change surname\n2 - Change first name\n3 - Change position\n4 - Change phone\n5 - Change salary')
    print('=' * 30)
    match int(input('Choose among the changes: ')):
        case 1:
            data[index]['surname'] = input('-> Изменить фамилию: ')
        case 2:
            data[index]['first_name'] = input('-> Изменить имя: ')
        case 3:
            data[index]['position'] = input('-> Изменить должность: ')
        case 4:
            data[index]['phone'] = input('-> Изменить телефон: ')
        case 5:
            data[index]['salary'] = int(input('-> Изменить зарплату: '))
    
