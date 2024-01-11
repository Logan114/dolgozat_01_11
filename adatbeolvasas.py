from classok import Stadionok
stadionok_lista = []
file = open("stadionok.txt","r")
sorok = file.readlines()[1:]

def feldolgozas(sorok):
    for i in range(0,len(sorok),1):
        jelen_sor = sorok[i]
        feldolgozott = jelen_sor.strip().split(";")
        nev = feldolgozott[0]
        varos = feldolgozott[1]
        csapat = feldolgozott[2]
        elso = feldolgozott[3]
        utolso = feldolgozott[4]
        stadion = Stadionok(nev,varos,csapat,elso,utolso)
        stadionok_lista.append(stadion)
    return stadionok_lista

def csapatok_szama(lista):
    csapat_ossz:int = int(0)
    for i in range(0,len(lista),1):
        csz:int = int(lista[i].csapat)
        csapat_ossz += csz
    print (f"A csapatok száma: {csapat_ossz}")

def NewYork(lista):
    for i in range(0,len(lista),1):
        if lista[i].varos == "New York":
            print(f"{lista[i].csapat}, {lista[i].nev}")
            

