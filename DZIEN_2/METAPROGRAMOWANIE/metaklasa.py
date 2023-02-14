class MojaMeta(type):

    def __new__(cls, nazwa, dziedziczenie, atrybuty):
        print(f"nazwa klasy: {nazwa}")
        print(f"dziedziczone klasy: {dziedziczenie}")
        print(f"słownik atrybutów: {atrybuty}")
        return type.__new__(cls, nazwa, dziedziczenie, atrybuty)


class Podstawowa:
    pass


class Pierwsza(Podstawowa,metaclass=MojaMeta):
    @property
    def info(self):
        return "informacja"

class Druga(Pierwsza):
    pass

class Ekstra:
    pass

class Trzecia(Ekstra,Druga):
    def msh(self,m):
        return m


#ABC -> ABCMeta
