def adatok_bekerese():
    jel = input("Adja meg a műveleti jelet (+, -, /, *): ")
    while jel not in ("+", "-", "/", "*"):
        print("Nem megfelelő input\nKérek másikat")
        jel = input("Adja meg a műveleti jelet (+, -, /, *): ")

    while True:
        try:
            szam1 = int(input("Adja meg az első számot: "))
            break
        except ValueError:
            print("Nem számot adtál meg, kérlek próbáld újra.")

    while True:
        try:
            szam2 = int(input("Adja meg a második számot: "))
            break  # A kimenet megfelelő, kilépünk a ciklusból
        except ValueError:
            print("Nem számot adtál meg, kérlek próbáld újra.")

    return jel, szam1, szam2


def muveletek_vegrehajtasa(jel, szam1, szam2):
    if jel == "+":
        return szam1 + szam2
    elif jel == "-":
        return szam1 - szam2
    elif jel == "*":
        return szam1 * szam2
    elif jel == "/":
        if szam2 != 0:
            return szam1 / szam2
        else:
            return "Nem lehet osztani nullával."


def eredmenyek_megejelenitese(eredmeny):
    print(f"Az eredmény: {eredmeny}")
    exit()


# Program fő része
jel, szam1, szam2 = adatok_bekerese()
eredmeny = muveletek_vegrehajtasa(jel, szam1, szam2)
eredmenyek_megejelenitese(eredmeny)

