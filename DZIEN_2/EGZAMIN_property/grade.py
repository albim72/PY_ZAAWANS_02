class Grade:
    def __init__(self):
        self._value = 0
        
    def __get__(self, instance, owner):
        return self._value
    
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Ocena musi być z zakresu 0-100')
        self._value = value
        
class NewExam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
