from ispit import unos_ispita, ispis_ispita
from kolegij import unos_kolegija

kolegij = []
ispiti = []

broj_kolegija = int(input("Unesi broj kolegija:"))
for i in range(1, broj_kolegija + 1):
    kolegij.append(unos_kolegija(i))

broj_ispita = int(input('Unesite broj ispita: '))
for i in range(1, broj_ispita+1):
    ispiti.append(unos_ispita(kolegij, i))

for ispit in ispiti:
    ispis_ispita(ispit)
