from homework8_view import show_menu as ui
from homework8_module import read_database as read_db
from homework8_module import read_deleted as read_dbd
from homework8_module import find_employee
from homework8_module import find_fired
from homework8_module import select_position
from homework8_module import select_salary
from homework8_module import add_employee
from homework8_module import del_employee
from homework8_module import upd_employee
from homework8_module import exp_data_json
from homework8_module import exp_data_csv

def controller():
    item = -1
    while item != 0:
        item = ui()
        data = read_db()
        data_d = read_dbd()
        match item:
            case 1:
                find_employee(data)
            case 2:
                find_fired(data_d)
            case 3:
                select_position(data)
            case 4:
                select_salary(data)
            case 5:
                add_employee(data, data_d)
            case 6:
                del_employee(data, data_d)
            case 7:
                upd_employee(data)
            case 8:
                exp_data_json(data)
            case 9:
                exp_data_csv(data)
    else:
        print("Status: work completed")
