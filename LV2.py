from datetime import date
kolegij = {}
ispit = {}
student = {}
kolegij['predmet'] = input("Unesite ime kolegija:").upper()
kolegij['ects'] = int(input("Unesite ECTS bodove za kolegij: "))
print("Kolegij",kolegij['predmet'],"nosi",kolegij['ects'],"ECTS bodova.")

ispit['kolegij'] = kolegij
ispit['dan'] = int(input("Unesite dan ispita:"))
ispit['mjesec'] = int(input("Unesite mjesec ispita:"))
ispit['godina'] = int(input("Unesite godinu ispita:"))
ispit['datum'] = date(ispit['godina'],ispit['mjesec'],ispit['dan'])
print("Kolegij",ispit['kolegij']['predmet'],"nosi",ispit['kolegij']['ects'],"ECTS bodova.")
print("Datum ispita je",ispit['datum'])

student['ime'] = input("Unesite ime studenta:").capitalize()
student['prezime'] = input("Unesite prezime studenta:").capitalize()
student['ispit'] = ispit
print("Student ",student['ime'],student['prezime'],
      "\nje prijavio ispit iz kolegija",student['ispit']['kolegij']['predmet'],
    "\nkoji će se održati:",student['ispit']['datum'])
