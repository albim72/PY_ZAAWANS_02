from dataclasses import dataclass

class Liczba:
    def __init__(self,x):
        self.x=x

zk = Liczba(9)
print(zk.x)

@dataclass
class DLiczba:
    x:int

dk = DLiczba(56)
print(dk.x)

# class SLiczba:
#     x:int
#
# s = SLiczba(11)
# print(s.x)

@dataclass
class Dane:
    nazwa:str
    licznik:int=0
    cena:float=0.0

prod = Dane("pudłko 22",6,11.25)
print(f'{prod.nazwa} -> cena: {prod.cena} zł, {prod.licznik} sztuk')
