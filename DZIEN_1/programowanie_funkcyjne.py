#przykład 1
def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu...")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka")

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} w urodziny")

dmuchanie("świeczek na torcie")

#przykład2

def nowyuczestnik(imie):
    return f"Miło Cię powitać na evencie {imie}"

def wystapienie(imie,nrsali):
    return f"Wystąpienie prelegenta: {imie} , nr sali -> {nrsali}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(nowyuczestnik,"Leon"))
print(osoba(wystapienie,"Anna",7))
