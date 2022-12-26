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
from homework8_module import exp_data_txt

def controller():
    item = -1
    while item != 0:
        item = ui()
        data = read_db()
        data_d = read_dbd()
        if item == 1:
            find_employee(data)
        if item == 2:
            find_fired(data_d)
        if item == 3:
            select_position(data)
        if item == 4:
            select_salary(data)
        if item == 5:
            add_employee(data, data_d)
        if item == 6:
            del_employee(data, data_d)
        if item == 7:
            upd_employee(data)
        if item == 8:
            exp_data_json()
        if item == 9:
            exp_data_txt()
    else:
        print("Status: work completed")
