from datetime import date
kolegiji = []
broj_kolegija = int(input("Unesite broj kolegija:"))
for i in range(broj_kolegija):
    kolegij = {}
    kolegij['ime'] = input("Unesite ime kolegija: ")
    kolegij['ects'] = int(input(f"Unesite ECTS bodove za {i + 1}. kolegij: "))
    kolegiji.append(kolegij)

#print("Popis svih kolegija:")
# kolegij in kolegiji:
    #print(f"\tKolegij {kolegij['ime']} nosi {kolegij['ects']} ECTS bodova ")

ispiti = []
broj_ispita = int(input("Unesite broj ispita:"))

print('Popis kolegija: ')
for i, kolegij in enumerate(kolegiji):
    print(f"{i+1}. {kolegij['ime']}")

for j in range(broj_ispita):
    odabir_kolegija = int(input('Unesite kolegij: '))
    dan = int(input('Unesite dan ispita: '))
    mjesec = int(input('Unesite mjesec ispita: '))
    godina = int(input('Unesite godinu ispita: '))
    datum = date(godina, mjesec, dan)
    ispiti.append({'kolegij': kolegiji[odabir_kolegija-1], 'datum': datum})
print(f"\tIspit iz kolegija {ispiti['kolegiji']['ime']}, koji nosi {ispiti['kolegiji']['ime']} ECTS bodova održati će se{ispiti['kolegiji']['ime']}")




