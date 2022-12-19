def export_txt():
    read_data = 'homework7_book.csv'
    write_data = 'homework7_book.txt'
    with open(read_data, 'r') as rf, open(write_data, 'w') as wf:
        for line in rf:
            wf.write(line)

def export_csv():
    read_data = 'homework7_book.txt'
    write_data = 'homework7_book.csv'
    with open(read_data, 'r') as rf, open(write_data, 'w') as wf:
        for line in rf:
            wf.write(line)
