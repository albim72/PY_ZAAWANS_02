from dataclasses import dataclass,astuple,asdict,field

@dataclass(order=True)
class Person:
    firstname:str = "Jan"
    lastname:str = "Kowalski"
    age:int = 41
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)
    sort_index:int = field(init=False,repr=False)

    def __repr__(self):
        return f"Pracownik: {self.firstname } {self.lastname}, wiek: {self.age}, " \
               f"stanowisko pracy: {self.job}. -> {self.full_name}"

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname
        self.sort_index = self.age
        self.sort_index = self.job

janek = Person()
print(janek)
print(astuple(janek))
print(asdict(janek))

print(janek.full_name)

olga = Person("Olga","Kot",33,"sekretarka")
print(olga)
print(olga.full_name)

janek_n = Person(job="Project Manager",age=43)
print(janek_n)

print(janek_n>janek)

olga_n = Person("Olga","Kot",38,"Dyrektor ds finansów")
print(olga_n<olga)

print(janek_n>olga)

janek_n2 = Person(age=18,job="kierowca")
print(janek_n2)

print(janek_n2>janek)

