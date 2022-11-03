import sqlite3, datetime
from jsonconverter import convert_json
import json



### ДОБАВЛЕНИЕ ДАННЫХ О ДОХОДЕ (ЗАРПЛАТА/ЧАЕВЫЕ/ПОДРАБОТКА/ПРОДАЖА ЧЕГО-ЛИБО)
#########
def add_income(name, sum):
    try:
        conn = sqlite3.connect('receipts.db')
        cur = conn.cursor()
        sqlite_insert = """INSERT INTO income VALUES(?, date(), ?);"""
        data_values = (name, sum)
        cur.execute(sqlite_insert, data_values)
        conn.commit()
        cur.close()
    except sqlite3.Error as error:
        print('Ошибка', error)
    finally:
        if conn:
            conn.close()

#add_income('mommy', 5000)
### ADD A SAVING SUMM WITH DATE AND TYPE OF SAVING: CONTRIBUTION, BROKERAGE ACCOUNT ETC.
#######

def add_savings(name, date, sum):
    try:
        conn = sqlite3.connect('receipts.db')
        cur = conn.cursor()
        sqlite_insert = """INSERT INTO savings VALUES(?, ?, ?);"""
        data_values = (name, date, sum)
        cur.execute(sqlite_insert, data_values)
        conn.commit()
        cur.close()
    except sqlite3.Error as error:
        print('Ошибка', error)
    finally:
        if conn:
            conn.close()



######ВЫВОД ДАННЫХ ИЗ ТАБЛИЦЫ ДОХОДОВ С ИСПОЛЬЗОВАНИЕМ НАЗВАНИЯ КАТЕГОРИИ (ЗАРПЛАТА, ЧАЕВЫЕ, ПРОДАЖИ, ПОДРАБОТКИ И Т.Д.)
###### ПЛЮС ВЫБОРКА ПО ДАТЕ (ОТ НАЧАЛЬНОЙ ДАТЫ включительно, ДО КОНЕЧНОЙ включительно)

def income_output(type, date1, date2):
    try:
        conn = sqlite3.connect('receipts.db')
        cur = conn.cursor()
        sqlite_output = """SELECT sum FROM income WHERE name = ? and date BETWEEN ? and ?"""
        cur.execute(sqlite_output, (type, date1, date2,))
        records = cur.fetchall()
        counter = 0
        for i in records:
            counter += i[0]
        return counter
        cur.close()
    except sqlite3.Error as error:
        print('Ошибка', error)
    finally:
        if conn:
            conn.close()



def new_category(name, category):
    with open('categories.json', 'r', encoding='UTF-8') as file_output:
        data = json.load(file_output)
    try:
        data[0][category].append(name)
    except:
        data[0][category] = []
        data[0][category].append(name)
    with open('categories.json', 'w', encoding='UTF-8') as write_file:
        json.dump(data, write_file)


def set_category(name):
    with open('categories.json', encoding='UTF-8') as file:
        data = json.load(file)
        flag = False
        for key, value in data[0].items():
            for val in value:
                if name == val:
                    flag = True
                    return key
    if not flag:
        print('Нужно выбрать категорию для:', name)
        category = input()
        new_category(name, category)
        return category


def add_receipts():
    try:
        data = convert_json()
        conn = sqlite3.connect('receipts.db')
        cur = conn.cursor()
        for i in data:
            name = i[1]
            date = i[0]
            summ = i[2] // 100
            category = set_category(name)
            sqlite_insert = """INSERT INTO losts VALUES (?, ?, ?, ?);"""
            cur.execute(sqlite_insert, (category, name, date, summ,))
            conn.commit()
        cur.close()
    except sqlite3.Error as error:
        print('Ошибка:', error)



if __name__ == '__main__':
    add_receipts()