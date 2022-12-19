import random

surnames = ['Bulgakov', 'Pushkin', 'Lermontov', 'Nekrasov', 'Chekhov', 'Dostoevsky']
names = ['Michael', 'Alexander', 'Viktor', 'Nicholas', 'Anton', 'Fedor']
descriptions = ['worker', 'manager', 'logistics', 'recruiter', 'accountant', 'lawyer']

def create_book(k):
    if k == 1:
        file = open('homework7_book.txt', 'w')
        newentry = "id,surname,name,phone,description\n" + '\n'
        file.writelines(newentry)
    if k == 2:
        file = open('homework7_book.csv', 'w')
        newentry = "id,surname,name,phone,description\n" + '\n'
        file.writelines(newentry)
    for i in range(10):
        a = f'{str(i + 1)},{creator_entry()}\n' + '\n'
        file.write(a)
    file.close()

def creator_entry():
    s = ""
    s = s + random.choice(surnames) + ',' + random.choice(names) + ',' + \
        phones() + ',' + random.choice(descriptions)
    return s

def phones():
    s = '+'
    random_phone = random.randint(79100000000, 79200000000)
    s = s + str(random_phone)
    return s
