def unos_kolegija(redni_broj):
    kolegij = {}

    kolegij['ime'] = input(f"Unesite ime {redni_broj}.  kolegija: ")
    kolegij['ECTS'] = int(input(f"Unesite ECTS bodove za {redni_broj}. kolegij: "))

    return kolegij

