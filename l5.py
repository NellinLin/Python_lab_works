# Вариант 10
# Связь один-ко-многим

import random

class Sotrudnik:
    def __init__(self,ID_S=None,Fam=None,ID_O=None):
        self.ID_S=ID_S
        self.Fam=Fam
        self.ID_O=ID_O

    def print_sotrudnik(self):
        print("{0}  {1}  {2}".format(self.ID_S,self.Fam,self.ID_O))


class Otdel:
    def __init__(self,ID_O=None, Name_O=None, stl_sotrudniki=None):
        self.ID_O=ID_O
        self.Name_O=Name_O
        self.Stl_sotr=stl_sotrudniki
        
    def print_otdel(self):
        print("{0} {1}\nСотрудники: {2}".format(self.ID_O,self.Name_O,self.Stl_sotr))

    def print_sotr_fam_A(self):
        for s in self.Stl_sotr:
            if s.Fam[0]=='A': print("   ",s.Fam)
            
    def print_kol_sotr(self):
        print("\nКол-во число сотрудников отдела {0} {1}:".format(self.ID_O,self.Name_O))
        print("   ",len(self.Stl_sotr))

    def vse_sotr_A(self):
        k=0
        for s in self.Stl_sotr:
            if s.Fam[0]=='A': k+=1
        if k==len(self.Stl_sotr):
            print('\t{0}'.format(self.Name_O))
            return 1
        return 0

    def h_A(self):
        k=0
        for s in self.Stl_sotr:
            if s.Fam[0]=='A': k+=1
        if k>0:
            print('\t{0}'.format(self.Name_O))
            return 1
        return 0

    def sort_sotr(self):
        st_s=[]
        for x in self.Stl_sotr:
            st_s.append(x.Fam)
        st_s.sort()
        print("\nОтдел:{0}".format(self.Name_O))
        for x in st_s:
             print("   ",x)
        
# ФУНКЦИИ
#__________________________________________________________________________

def print_sotr_na_A(stl_otd):
    print("\nСотрудники (фамилия начинается на A):")
    for o in stl_otd:
        o.print_sotr_fam_A()
    
def otd_vse_sotr_A(stl_otd):
    print("\nОтделы,все сотрудники которых на А:")
    k=0
    for o in stl_otd:
        k+=o.vse_sotr_A()
    if k==0:
        print("\tТаких нет")

def otd_h_o_sotr_A(stl_otd):
    print("\nОтделы,хотя бы один сотр. на А:")
    k=0
    for o in stl_otd:
        k+=o.h_A()
    if k==0:
        print("\tТаких нет")

def print_sotr_po_otd(stl_otd):
    for o in stl_otd:
        o.sort_sotr()

#MAIN
#__________________________________________________________________________

sot=[] #Список со всеми сотрудниками
fam_s=["Anderson","Armstrong","Artic","Basic","Vant","Adit","Abant","Kurt","Vening","Aster","Alias","Apple"]
id_o=[0,1,2]

for i in range(10):
    sot.append(Sotrudnik(i,(random.choice(fam_s)),(random.choice(id_o))))
    
for x in sot:
    x.print_sotrudnik()

otd0=[]; otd1=[]; otd2=[] #Списки с сотрудниками по отделам
for x in sot:
    if x.ID_O==0: otd0.append(x)
    if x.ID_O==1: otd1.append(x)
    if x.ID_O==2: otd2.append(x)

Otd_Name=["Programming","SoftWare","Frontend"] #Список с отделами
otd=[]
otd.append(Otdel(0,Otd_Name[0],otd0))
otd.append(Otdel(1,Otd_Name[1],otd1))
otd.append(Otdel(2,Otd_Name[2],otd2))

#__________________________________________________________________________

# ТЕСТ ФУНКЦИЙ

# Вывести всех сотрудников, фамилия которых на А
print_sotr_na_A(otd)

# Выведите список всех отделов и кол-во сотрудников в них
for o in otd:
    o.print_kol_sotr()

# Отделы, все сотрудники которого на А
otd_vse_sotr_A(otd)

# Отделы, где хотя бы один сотрудник на А
otd_h_o_sotr_A(otd)

# Вывести сотрудников (отсортировать их) по отделам 
print_sotr_po_otd(otd)
