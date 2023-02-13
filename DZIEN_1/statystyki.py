liczby = [56,245,-66,0,12,1987,-999,112,87,234,-87,555,-222,0,456,12]
liczbykrt = (99,3345,2,5,-23,3,3)
liczbyzb = {45,67,-8,9,9,9,0,2,3,4,2,3,45,3,0}

print(set(liczbyzb))
liczbyT = list(liczbyzb)
# liczbyT.sort()
# print(liczbyT)
print(sorted(liczbyT))
print(liczbyT)

def pokaz_statystyki(kolekcja):
    minimum = min(kolekcja)
    maksimum = max(kolekcja)
    rozstep = maksimum - minimum
    l_elem = len(kolekcja)
    sumael = sum(kolekcja)
    sr_arytm = sumael/l_elem
    return minimum,maksimum,rozstep,l_elem,sumael,sr_arytm

wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

wynik = pokaz_statystyki(liczbykrt)
print(wynik)
print(type(wynik))

wynik = pokaz_statystyki(liczbyzb)
print(wynik)
print(type(wynik))

mini, maxi,roz, lb,sm,avg = pokaz_statystyki(liczby)
print(f"największa wartość: {maxi}, najmniejsza wartość: {mini}, rozstęp: {roz}, "
      f"liczba elementów: {lb}, suma wartości: {sm}, średnia arytmetyczna: {avg}")
