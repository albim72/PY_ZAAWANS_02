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
