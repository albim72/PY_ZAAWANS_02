from collections import namedtuple

Student = namedtuple('Student',['name','age','stud_nb'])

s = Student('Jan Kot','21',45435)
print(s)

print(f"wiek studenta = {s[1]} lat")
print(f"imię i nazwisko studenta: {s.name}")
print(f"nr studenta: {getattr(s,'stud_nb')}")
