import dane
# import dane as dn
from dane import nb as filia
from dane import book as ksiazka

from funkcje.bfunkcje import czytaj_liste,czytaj_slownik



print("____________czytanie bezpośrednie_____________")
print(filia)
print(ksiazka)
print("____________czytanie z użyciem funckji_____________")
czytaj_liste(filia)
czytaj_slownik(ksiazka)
