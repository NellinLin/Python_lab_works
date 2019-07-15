import math
import statistics
import sys
import os

def give_data(s):
    try:
        file=open(s,"r")
    except IOError:
        print('Ошибка чтения файла1')
        sys.exit(0)

    str=''
    if os.stat(s).st_size==0:
        print ("Файл пуст")
        sys.exit(0)
        
    while 1:                        # Составление строки из всех файлов
        name_f=file.readline()
        if name_f=="":break

        name_f=name_f.replace('\n','')
        try:
            f=open(name_f,"r")
        except IOError:
            print('Ошибка чтения файла2')
            sys.exit(0)
            
        str=str+' ' +f.readline()
        f.close()

    file.close()

    str=str.split(' ')              # Удаление всех неправильных элементов
    data=[]
    for dat in range(len(str)):
        try:
            str[dat]=float(str[dat])
        except ValueError:
            continue
        else:
            data.append(str[dat])
    str.clear()
    return data


def median(dat):
    dat.sort()
    if len(dat)%2==0:
        return ((dat[len(dat)//2-1]+dat[len(dat)//2])/2)
    else:
        return dat[len(dat)//2]

def rate(dat):                  # Вывод 3( или менее ) часто встречающихся цифр
    sl={}
    for i in range(len(dat)):
        k=0
        for d in dat:
            if d==dat[i]:k+=1
        sl[dat[i]]=k

    z=sorted(sl.items(), key=lambda item: (-item[1], item[0]))
    if len(dat)>=3:
        big_data=[z[0][0],z[1][0],z[2][0]]
        return big_data
    else:
        big_data=[]
        for x in z:
            big_data.append(x[0])
        return big_data

def otklon(dat):                # Подсчёт стандартного отклонения
    sred=sum(dat)/len(dat)
    otkl=0
    for d in dat:
        otkl=otkl+(d-sred)**2
    otkl=math.sqrt(otkl/(len(dat)-1))
    return otkl

def mean (dat):
    return sum(dat)/len(dat)
    
#Тело программы

data = give_data("files.txt")
print(data)
print('count = ', len(data))
print('mean = ' ,mean(data))
print('median = ', median(data))
print('mode = ', rate(data))
print('str.dev. = %.2f' %(otklon(data)))

print('\n\nИспользование statistics')
print('count = ', len(data))
print('mean = ' ,statistics.mean(data))
print('median = ', statistics.median(data))
print('mode = ', rate(data))
print('str.dev. = %.2f' %(statistics.stdev(data)))
