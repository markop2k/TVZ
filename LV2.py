from datetime import date
kolegij = {}
ispit = {}
student = {}
kolegij['predmet'] = input("Unesite ime kolegija:")
kolegij['ects'] = int(input("Unesite ECTS bodove za kolegij: "))
#print("Kolegij",kolegij['predmet'].upper(),"nosi",kolegij['ects'],"ECTS bodova.")

ispit['predmet'] = kolegij['predmet']
ispit['ects'] = kolegij['ects']
ispit['dan'] = int(input("Unesite dan ispita:"))
ispit['mjesec'] = int(input("Unesite mjesec ispita:"))
ispit['godina'] = int(input("Unesite godinu ispita:"))
ispit['datum'] = date(ispit['godina'],ispit['mjesec'],ispit['dan'])
#print("Kolegij",ispit['predmet'].upper(),"nosi",ispit['ects'],"ECTS bodova.")
#print("Datum ispita je",ispit['datum'])

student['ime'] = input("Unesite ime studenta:")
student['prezime'] = input("Unesite prezime studenta:")
student['predmet'] = ispit['predmet']
student['ects'] = ispit['ects']
student['datum'] = ispit['datum']
print("Student ",student['ime'].capitalize(),student['prezime'].capitalize())
print("je prijavio ispit iz kolegija",student['predmet'].upper())
print("koji će se održati:",student['datum'])
