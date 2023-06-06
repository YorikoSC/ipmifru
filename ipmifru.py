#!/usr/bin/python3.11
import subprocess
from sys import executable

dev = int(input('Выбирете производителя: Gigabyte(1) или ASUS(2): '))#Выбор девелопера.
if dev == 1:
        loc = int(input('Выбирете режим: Локально(1) или удалённо(2): '))
elif dev == 2: #Асуса нет
        print ('Данный функционал на данный момент не реализован')
        quit()

def data(): #Ввод и проверка данных до передачи в переменные функций-редакторов
    while True:
        resp = input()
        if resp:
            confirm = input(f"{resp} - давнные верны? (y/n)?")
            if confirm.lower() == 'y':
                return resp
        print ('Повторите ввод')
    
def multifru_net(): #Функция обновления полей(удаленно) при наличии двух FRU на сервере
    print ('Модель шасси (производителя): ')
    CPN = data()
    print ('Серийник шасси: ')
    CSN = data()
    print ('Имя сервера: ')
    PN = data()
    print ('Парт номер(ТИС): ')
    PPN = data()
    print ('Серийный номер(ТИС): ')
    PSN = data()
    print ('Asset tag: ')
    PAT = data()
    processCPN_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'c', '0', CPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCPN_0.stdout)
    processCSN_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'c', '1', CSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCSN_0.stdout)
    processPN_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'p', '1', PN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPN_0.stdout)
    processPPN_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'p', '2', PPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPPN_0.stdout)
    processPSN_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'p', '4', PSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPSN_0.stdout)
    processPAT_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'p', '5', PAT], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPAT_0.stdout)
    processCPN_1 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '1', 'field', 'c', '0', CPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCPN_1.stdout)
    processCSN_1 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '1', 'field', 'c', '1', CSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCSN_1.stdout)
    processPN_1 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '1', 'field', 'p', '1', PN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPN_1.stdout)
    processPPN_1 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '1', 'field', 'p', '2', PPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPPN_1.stdout)
    processPSN_1 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '1', 'field', 'p', '4', PSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPSN_1.stdout)
    processPAT_1 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '1', 'field', 'p', '5', PAT], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPAT_1.stdout)
    frulist = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'list'], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')# Команда вывода общего списка заполненных полей
    print(frulist.stdout)
    checkback = input('Всё верно?(y/n): ')#Подтверждение правильности ввода.
    if checkback == 'n':
       process = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'shell'])
    else:
       print('Обновление завершено. Произведите сброс питания и убедитесь в фиксации заданных параметров!')
       quit()
       
def siglefru_net():#Функция обновления полей(удалённо) при наличии одного FRU на сервере
    print ('Модель шасси (производителя): ')
    CPN = data()
    print ('Серийник шасси: ')
    CSN = data()
    print ('Имя сервера: ')
    PN = data()
    print ('Парт номер(ТИС): ')
    PPN = data()
    print ('Серийный номер(ТИС): ')
    PSN = data()
    print ('Asset tag: ')
    PAT = data()/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'c', '0', CPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCPN_0.stdout)
    processCSN_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'c', '1', CSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCSN_0.stdout)
    processPN_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'p', '1', PN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPN_0.stdout)
    processPPN_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'p', '2', PPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPPN_0.stdout)
    processPSN_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'p', '4', PSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPSN_0.stdout)
    processPAT_0 = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'edit', '0', 'field', 'p', '5', PAT], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPAT_0.stdout)
    frulist = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'fru', 'list'], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')# Команда вывода общего списка заполненных полей
    print(frulist.stdout)
    checkback = input('Всё верно?(y/n): ')#Подтверждение правильности ввода.
    if checkback == 'n':
       process = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'shell'])
    else:
       print('Обновление завершено. Произведите сброс питания и убедитесь в фиксации заданных параметров!')
       quit()

def multifru_local(): #Функция обновления полей(локально) полей при наличии двух FRU на сервере
    print ('Модель шасси (производителя): ')
    CPN = data()
    print ('Серийник шасси: ')
    CSN = data()
    print ('Имя сервера: ')
    PN = data()
    print ('Парт номер(ТИС): ')
    PPN = data()
    print ('Серийный номер(ТИС): ')
    PSN = data()
    print ('Asset tag: ')
    PAT = data()
    processCPN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'c', '0', CPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCPN_0.stdout)
    processCSN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'c', '1', CSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCSN_0.stdout)
    processPN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'p', '1', PN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPN_0.stdout)
    processPPN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'p', '2', PPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPPN_0.stdout)
    processPSN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'p', '4', PSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPSN_0.stdout)
    processPAT_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'p', '5', PAT], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPAT_0.stdout)
    processCPN_1 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '1', 'field', 'c', '0', CPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCPN_1.stdout)
    processCSN_1 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '1', 'field', 'c', '1', CSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCSN_1.stdout)
    processPN_1 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '1', 'field', 'p', '1', PN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPN_1.stdout)
    processPPN_1 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '1', 'field', 'p', '2', PPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPPN_1.stdout)
    processPSN_1 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '1', 'field', 'p', '4', PSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPSN_1.stdout)
    processPAT_1 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '1', 'field', 'p', '5', PAT], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPAT_1.stdout)
    frulist = subprocess.run(['/usr/bin/ipmitool', 'fru', 'list'], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')# Команда вывода общего списка заполненных полей
    print(frulist.stdout)
    checkback = input('Всё верно?(y/n): ')#Подтверждение правильности ввода.
    if checkback == 'n':
       process = subprocess.run(['/usr/bin/ipmitool', 'shell'])
    else:
       print('Обновление завершено. Произведите сброс питания и убедитесь в фиксации заданных параметров!')
       quit()
       
def siglefru_local():#Функция обновления полей(локально) при наличии одного FRU на сервере
    print ('Модель шасси (производителя): ')
    CPN = data()
    print ('Серийник шасси: ')
    CSN = data()
    print ('Имя сервера: ')
    PN = data()
    print ('Парт номер(ТИС): ')
    PPN = data()
    print ('Серийный номер(ТИС): ')
    PSN = data()
    print ('Asset tag: ')
    PAT = data()
    processCPN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'c', '0', CPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCPN_0.stdout)
    processCSN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'c', '1', CSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processCSN_0.stdout)
    processPN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'p', '1', PN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPN_0.stdout)
    processPPN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'p', '2', PPN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPPN_0.stdout)
    processPSN_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'p', '4', PSN], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPSN_0.stdout)
    processPAT_0 = subprocess.run(['/usr/bin/ipmitool', 'fru', 'edit', '0', 'field', 'p', '5', PAT], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(processPAT_0.stdout)
    frulist = subprocess.run(['/usr/bin/ipmitool', 'fru', 'list'], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')# Команда вывода общего списка заполненных полей
    print(frulist.stdout)
    checkback = input('Всё верно?(y/n): ')#Подтверждение правильности ввода.
    if checkback == 'n':
       process = subprocess.run(['/usr/bin/ipmitool', 'shell'])
    else:
       print('Обновление завершено. Произведите сброс питания и убедитесь в фиксации заданных параметров!')
       quit()
       
def local_srv(): #Функция локального обновления FRU
    com = str(input('Шьём весь FRU (y/n): '))
    if com == ('n'):
        process = subprocess.run(['/usr/bin/ipmitool', 'shell'])
    elif com == ('y'):
        frucount = int(input('Количество FRU на сервере: '))
    if frucount == 1:
        singlefru_local()
    elif frucount == 2:
        multifru_local()
    else:
        print ('Введено недопустимое значение')
        return
            
def remote_srv(): #Функция удалённого обновления FRU
    com = str(input('Шьём весь FRU (y/n): '))
    if com == ('n'):
        process = subprocess.run(['/usr/bin/ipmitool', '-I', 'lanplus', '-H', ip, '-U',login, '-P', pwd, 'shell'])
    elif com == ('y'):
        frucount = int(input('Количество FRU на сервере: '))
    if frucount == 1:
        singlefru_net()
    elif frucount == 2:
        multifru_net()
    else:
        print ('Введено недопустимое значение')
        return
            
if loc == 2:
    ip = str(input('введите IP сервера: '))
    login = str(input('Введите логин: '))
    pwd = str(input('Введите пароль: '))
    remote_srv()
    
elif loc == 1:
    login = str(input('Введите логин: '))
    pwd = str(input('Введите пароль: '))
    local_srv()