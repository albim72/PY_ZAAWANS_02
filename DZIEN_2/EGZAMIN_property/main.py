from homework import Homework
from exam import Exam
from grade import NewExam


print("________________ HOMEWORK _______________")
ga = Homework()
ga.grade = 98
assert ga.grade != 97
print(ga.grade)

print("________________ EXAM _______________")
hk = Exam()
hk.writing_grade = 77
hk.math_grade =70
assert hk.writing_grade == 77
assert hk.math_grade == 70
print(f'oceny -> pisanie: {hk.writing_grade}, matematyka: {hk.math_grade}')

print("________________ NEWEXAM _______________")
fexam = NewExam()
fexam.writing_grade = 81
fexam.math_grade = 46
fexam.science_grade = 54

print("________pierwsza ocena_____")
print(f'pisanie: {fexam.writing_grade}')
print(f'matematyka: {fexam.math_grade}')
print(f'nauka: {fexam.science_grade}')

print("________druga ocena_____")
sexam = NewExam()
sexam.writing_grade = 90
sexam.math_grade = 57
sexam.science_grade = 66
print(f'pisanie: {sexam.writing_grade}')
print(f'matematyka: {sexam.math_grade}')
print(f'nauka: {sexam.science_grade}')

print("mamy problem!!!")
print(f'ocena -> pierwsze podejście: {fexam.writing_grade}, ocena -> drugie podejście: {sexam.writing_grade}')
