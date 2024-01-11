szamok_lista = []
lista = []
ketjegyuek_lista = []
paros_osszege = []
paratlan_osszege = []
import random
def elso_feladat_a():
    n = 1
    while n % 2 != 0:
        n = int(input("Kérem adjon meg egy páros számot:"))
        if n%2 != 0:
            print("Ez nem páros szám! Adjon meg egy páros számot! ")

def elso_feladat_b():
    for i in range (0,3):
         n = 1
         while n%2 !=0:
            n = int(input(f"Kérem adja meg a(z) {i+1}. páros számot:"))
            if n%2 != 0:
                print(f"Ez nem páros szám! Adja meg a(z) {i+1}. páros számot:! ")
            else:
                szamok_lista.append(n)
    return szamok_lista

def elso_feladat_c(lista):
    minimum_ertek = min(lista)
    print(f"A legkissebb megadott szám értéke:{minimum_ertek}")

def masodik_feladat(lista):
    for i in range (0,14):
        lista.append(int(random.randrange(-40, 150)))
    print(f"A lista: {lista}")
    return lista

def masodik_feladat_b(lista, lista2):
    for i in range (0,(len(lista)),1):
        if len(str(lista[i])) == 2:
            lista2.append(lista[i])
    return lista2

def masodik_feladat_c(lista,paros):
    paros_ossz = 0
    for i in range (0,(len(lista)),1):
        if int(lista[i]) % 2 == 0:
            a = int(lista[i])
            paros_ossz =+ a
    paros.append(paros_ossz)
    return paros_osszege

def masodik_feladat_d(lista,paratlan):
    paratlan_ossz = 0
    for i in range (0,(len(lista)),1):
        if int(lista[i]) % 2 != 0:
            a = int(lista[i])
            paratlan_ossz =+ a
    paratlan.append(paratlan_ossz)
    return paratlan_osszege

def masodik_feladat_e(paratlan_list,paros_list):
    paratlan = paratlan_list
    paros = paros_list
    if paratlan > paros:
        print (f"A páratlanok összege {paratlan} > {paros}")
    else:
        print (f"A párosok összege {paros} > {paratlan} ")
        


#masodik_feladat(lista)
#masodik_feladat_c(lista, paros_osszege)
#masodik_feladat_d(lista,paratlan_osszege)
#masodik_feladat_e(paratlan_osszege, paros_osszege)