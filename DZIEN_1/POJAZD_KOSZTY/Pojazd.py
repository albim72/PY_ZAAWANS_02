from IPojazd import IPojazd
from ISilnik import ISilnik

class Pojazd(IPojazd,ISilnik):
    def spalanie(self, odl, litry):
        return litry*100/odl

    def kosztprzejazdu(self, odl, litry, cena_l):
        return self.spalanie(odl,litry)*(odl/100)*cena_l

    def dane_silnika(self, rodzaj, poj):
        return f"rodzaj: {rodzaj}, pojemność: {poj}"

    def stan(self, opis, ilekm, remonty):
        return f"stan silnika -> remonty: {remonty}, liczba przejechanych km: {ilekm}, " \
               f"informacje dodatkowe: {opis}"
    
