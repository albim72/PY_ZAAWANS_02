import time
import math

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

#przykład 3

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f'czas wykonania funkcji {funkcja.__name__}: {endtime-starttime} s')
    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper

@sleep
@pomiarczasu
def biglista():
    sum([i**3 for i in range(1000000)])

biglista()

@sleep
def info():
    return "opóźniona funkcja"

print(info())


#przykład 4
def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeater(n=6)
def komunikat(k,n):
    print(f'ważby komunikat nr {n}: {k}')

komunikat("fsdfdjfs5555555",78)

@repeater(11)
def hx(c):
    print((c-1)**6)

hx(3)
