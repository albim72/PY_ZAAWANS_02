from dataclasses import dataclass
from datetime import datetime

@dataclass
class NewPerson:
    first_name:str
    last_name:str
    year_of_birth:int
    #_age:int

    @property
    def age(self):
        #return datetime.now().year - self.year_of_birth
        return self._age

    @age.setter
    def age(self,nage):
        self._age = nage


p = NewPerson("Janusz","Gierej",1964)
# print(p)
# print(p.age)

p.age = 88
print(p)
print(p.age)
