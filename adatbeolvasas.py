nevek_lista = []
csapatok_lista = []
file = open("stadionok.txt","r")
sorok_lista = file.readlines()[1:]

def feldolgozas(lista):
    for i in range(0,len(lista),1):
        jelen_sor = lista[i]
        feldolgozott = jelen_sor.split.strip(";")
        nev = feldolgozott[0]
        varos = feldolgozott[1]
        csapat
def csapatok_szama(sorok,csapatok):
