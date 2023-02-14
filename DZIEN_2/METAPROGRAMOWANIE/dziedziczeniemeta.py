class MultiBases(type):
    def __new__(cls, clsname, bases, attrs):
        if len(bases) > 1:
            raise TypeError('Nie można wielodziedziczyć!')
        return super().__new__(cls, clsname, bases, attrs)


class Podstawowa(metaclass=MultiBases):
    pass

class Specjalna(Podstawowa):
    pass

class Dodatek:
    pass

class Finalna(Specjalna,Dodatek):
    pass
