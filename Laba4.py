import os

# Возвращает название файла с которым потом будет работа
def lst_file():
    lst =[i for i in list(os.listdir()) if ".lst" in i]
    if len(lst)==0:
        print ("Файлов с расширением .lst в каталоге нет")
        i=1
    else:
        i=1
        for f in lst:
            print('%d. ' %i,f)
            i+=1
        
    while True:
        num=input("Выберите номер файла (или 0 для создания нового файла): ")
        try:
            num=int(num)
            if num<0:
                raise ValueError("ERROR num < 0")
            elif num>i-1:
                raise ValueError("ERROR num > len")
            else:
                break
        except ValueError:
            print("ERROR input")
        
        
    if num==0:
        f_name=input("Выберите имя файла: ")+".lst"
        f=open(f_name,"w")
        f.close()
        return f_name
    
    return(lst[num-1])

# Добавление строки
def dobavit(stl):
    st=input('Добавить строку: ')
    stl.append(st)
    return stl

# Удаление строки по номеру
def udalit(stl):
    while True:
        num=int(input('Введите номер строки для удаления (или 0 для выхода): '))
        try:
            num=int(num)
            if num<0:
                raise ValueError("ERROR num < 0")
            elif num>len(stl):
                raise ValueError("ERROR num > len")
            else:
                break
        except ValueError:
            print("ERROR input")
        
    if num==0:
        return stl
    else:
        del stl[num-1]
        
    return stl

# Сохранение списка строк в файл    
def save(stl, f_name):
    f=open(f_name,"w")
    for x in stl:
        f.write(x)
    f.close()
    print('Сохранение ',len(stl),' строк в файл ',f_name)
    
# Выход с учётом сохранения
def exitt(stl,f_name):
    ch=input('Сохранить изменения (д/н): ')
    while ch not in ['Д','д','Н','н']:
        ch = input('Введите одну из команд:Дд,Нн : ')
    if ch=='Д' or ch=='д':
        save(stl,f_name)
    print('--Работа с файлом закончена--')

# Меню, в котором вызяваются функции
def menu(char, stl, f_name):
    if char=='Д' or char=='д':
        dobavit(stl)
    if char=='У' or char=='у':
        udalit(stl)
    if char=='С' or char=='с':
        save(stl,f_name)
    if char=='В' or char=='в':
        exitt(stl,f_name)
    
# Функция обработки приёма символа для действия
def take_char(count):
    if count==0:
        char=input('[Д]обавить [В]ыйти : ')
        while char not in ['Д','д','В','в']:
            char = input('Введите одну из команд:Дд,Вв : ')
    else:
        char=input('[Д]обавить [У]далить [С]охранить [В]ыйти : ')
        while char not in ['Д','д','У','у','С','с','В','в']:
            char = input('Введите одну из команд:Дд,Уу,Сс,Вв : ')
    

    return char
        
# Функция печати списка строк
def print_str(stl):
    print('\nСписок строк:')
    if len(stl)==0:
        print('--Список не содержит элементов--')
    else:
        i=1
        for x in stl:
            print('%d: '%i,x)
            i+=1
            
# Функция работы с файлом
def work_w_file(f_name):
    f=open(f_name,"r")
    stl_str=[]
    
    while True:
        stroka=f.readline()
        if stroka=='': break
        stl_str.append(stroka)
    f.close()
    
    while True:
        count=len(stl_str)
        print_str(stl_str)
        char=take_char(count)
        menu(char,stl_str, f_name)
        if char=='В' or char=='в': break
        


#Тело программы
file=lst_file()
print(file)
work_w_file(file)


