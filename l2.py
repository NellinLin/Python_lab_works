# Лабораторная работа №2, подготовила Шишова Анастасия СГН3-32

import math
import random
import sys

def write_points(kol, a, b):                # Функция записи точек
    try:                                    # в файл
        f_points=open("points.txt","w")
    except IOError:
        print("Ошибка чтения файла")
        sys.exit(0)

    for i in range(kol):
        x1=round(random.uniform(a, b), 2)
        y1=round(random.uniform(a, b), 2)
        x2=round(random.uniform(a, b), 2)
        y2=round(random.uniform(a, b), 2)
        
        f_points.write('%.2f %.2f %.2f %.2f\n'%(x1,y1,x2,y2))
        
    f_points.close()


def write_out(f, kol):                      # Функция вывода данных
    try:
        file=open(f,"r")
    except IOError:
        print("Ошибка чтения файла")
        sys.exit(0)

    for i in range(kol):
        stroka=file.readline()
        if stroka=="": break
        s=stroka.split(' ')
        print('{:3d}'.format(i+1),'{0:10.2f}'.format(float(s[0])),'{0:10.2f}'.format(float(s[1])),'{0:10.2f}'.format(float(s[2])),'{0:10.2f}'.format(float(s[3])))
        #print ('%d. ' %(i+1),stroka)
        
    file.close()  

def write_dl(f, kol):                      # Функция вывода данных
    try:
        file=open(f,"r")
    except IOError:
        print("Ошибка чтения файла")
        sys.exit(0)

    for i in range(kol):
        stroka=file.readline()
        if stroka=="": break
        print ('{:3d}'.format(i+1),'{0:10.4f}'.format(float(stroka)))
        
    file.close()
    
def dis_point_and_sr_znach(f):              # Функция среднего
    try:
        file=open(f,"r")
        outfile=open("distance.txt","w")
    except IOError:
        print("Ошибка чтения файла")
        sys.exit(0)

    c=k=0
    while 1:
        stroka=file.readline()
        if stroka=="": break
        s=stroka.split(' ')
        k+=1
        try:
            x1=float(s[0]); y1=float(s[1]); x2=float(s[2]); y2=float(s[3])
        except IndexError:
            print("Не введено значение, строка %d"%k)
            sys.exit(0)
        l1=math.sqrt((x1-x2)**2+(y1-y2)**2)
        c=c+l1
        outfile.write('%f\n'%l1)

    file.close()
    outfile.close()

    return c/k


# Тело программы

try:
    kol=int(input("Введите количество отрезков: "))
except ValueError:
    print("Введено не число")
    sys.exit(0)

try:
    print("Введите диапазон значений: ")
    a = float(input("a=")); b=float(input("b="))
except ValueError:
    print("Введено не число")
    sys.exit(0)

write_points(kol, a, b)

print("Точки:\n")
write_out("points.txt",kol)

sr = dis_point_and_sr_znach("points.txt")
print("Отрезки:\n")
write_dl("distance.txt",kol)
print("Среднее значение: ", sr)
