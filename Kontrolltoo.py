#1 задание

n = int(input("Введите число домов"))
for i in range(1, n+1):
    print(" ~~~~~", end=" ")
print()
for i in range(1, n+1):
    print('/_____\ ', end="")
print()
for i in range(1, n+1):
    print("| []  |", end=" ")
print()
for i in range(1, n+1):
    print(" -----", end=" ")

# 2 задание
#from random import *
#a=b=klass1=klass2=randint(15,30)
#summa=0
#while b>=0:
#    b-=1
#    n=randint(1,5)
#    summa+=n
#summa=summa/klass1
#print("Средний балл первого класса - ",round(summa,2))
#summa=0
#while a>=0:
#    a-=1
#    n=randint(1,5)
#    summa+=n
#summa=summa/klass2
#print("Средний балл второго класса - ",round(summa,2))

#3 задание

#from random import *
#a=0
#b=2
#klass=randint(20,30)
#while klass>0:
#    klass-=1
#    klass_1=uniform(1,5)
#    if a<klass_1:
#        a=0
#        a+=klass_1
#    elif b>klass_1:
#        b=0
#        b+=klass_1
#print("Наибольший балл - ", round(a,1))
#print("Наименьший балл - ", round(b,1))





#4 задание

#from random import *
#S=0
#for i in range(12):
#    a=randint(1000,40000)
#    b=randint(10,50)
#    S=0
#    S+=a/b
#    print("Среднеяя плотность населения данного района составляет: ",round(S,1))

#5 задание

