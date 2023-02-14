from decimal import Decimal


class Akwizytor:
    """
    pracownik, którego wynagrodzenie jest wyłącznie prowizją od sprzedaży
    """

    def __init__(self, imie, nazwisko, nr_ubezp, sprzedaz, prowizja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_ubezp = nr_ubezp
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self,noweimie):
        self._imie = noweimie

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nowenazwisko):
        self._nazwisko = nowenazwisko

    @property
    def nr_ubezp(self):
        return self._nr_ubezp

    @nr_ubezp.setter
    def nr_ubezp(self, nowe_ubezp):
        self._nr_ubezp = nowe_ubezp

    @property
    def sprzedaz(self):
        return self._sprzedaz

    @sprzedaz.setter
    def sprzedaz(self,kwota):
        if kwota<Decimal('0.00'):
            raise ValueError('wartość sprzedaży nie może być ujemna...')
        self._sprzedaz = kwota

    @property
    def prowizja(self):
        return self._prowizja

    @prowizja.setter
    def prowizja(self, procent):
        if not(Decimal('0.00')<procent<Decimal('30.00')):
            raise ValueError('wartość prowizji należy do zakresu 1-29')
        self._prowizja = procent

    def zarobek(self):
        return self.sprzedaz*(self.prowizja/Decimal('100.00'))

    def __repr__(self):
        return f"Akwizytor: {self.imie} {self.nazwisko}\n" \
               f"numer ubezpieczenia: {self.nr_ubezp:.2f} zł\n" \
               f"sprzedaż: {self.sprzedaz:.2f} zł\n" \
               f"prowizja: {self.prowizja:.2f} %"



