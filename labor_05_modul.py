from getpass import getpass



def felhasznalonev():
    username = input("Kérem a felhasználónevet(email): ")
    while " " in username or "@" not in username or "." not in username:
        print("Érvénytelen e-mail formátum!")
        if " " in username:
            print("Szóköz található a felhasználónévben!")
        if "@" not in username:
            print("Hiányzik a @ jel!")
        if "." not in username:
            print("Hiányzik a . jel!")
        username = input("Kérem a felhasználónevet: ")
    return username


def jelszo_bekerese():
    def jelszohossza(_password):
        return len(password) >= 8

    def szam(_password):
        for betu in password:
            if betu.isnumeric():
                return True
        return False

    def kisbetu(_password):
        ok=False
        for betu in _password:
            if betu.islower():
                ok=True
                break
        return ok

    def nagybetu(_password):
        ok=False
        for betu in _password:
            if betu.isupper():
                ok=True
                break
            return ok
    password = input("Kérek egy jelszót: ")
    while not jelszohossza(password) or not szam(password)  or not kisbetu(password) or not nagybetu(password):
        print(
            "Rossz a jelszó! A jelszónak legalább 8 karakter hosszúnak kell lennie, és tartalmaznia kell legalább egy számot.")
        password = input("Kérek egy jelszót: ")

    return password