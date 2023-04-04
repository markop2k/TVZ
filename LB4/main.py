from kolegij import unos_kolegija, ispis_kolegija
kolegiji = []

broj_kolegija = int(input('Unesite broj kolegija: '))
for i in range(1, broj_kolegija+1):
    kolegiji.append(unos_kolegija(i))

for kolegij in kolegiji:
    ispis_kolegija(kolegij)