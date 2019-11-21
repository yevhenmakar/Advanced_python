from abc import ABC, abstractmethod
from datetime import date


class Person(ABC):

    def __init__(self, last_name, birth, faculty):
        self._last_name = last_name
        self._birth = birth
        self._faculty = faculty

    @abstractmethod
    def get_info(self):
        print(f'Last name: {self._last_name}.\n'
              f'Date of birth: {self._birth}. \n'
              f'Faculty: {self._faculty}.')

    def get_last_name(self):
        return self._last_name

    def get_age(self):
        today_year, today_month, today_day = (str(date.today()).split('-'))
        birth_year, birth_month, birth_day = self._birth.split('.')
        return int(today_year) - int(birth_year) - ((today_month, today_day) < (birth_month, birth_day))


class Entrant(Person):

    def __init__(self, last_name, birth, faculty):
        super().__init__(last_name, birth, faculty)

    def get_info(self):
        super().get_info()
        print('')


class Student(Person):

    def __init__(self, last_name, birth, faculty, year):
        super().__init__(last_name, birth, faculty)
        self._year = year

    def get_info(self):
        super().get_info()
        print(f'Year: {self._year}. \n')


class Teacher(Person):

    def __init__(self, last_name, birth, faculty, position, experience):
        super().__init__(last_name, birth, faculty)
        self._position = position
        self._experience = experience

    def get_info(self):
        super().get_info()
        print(f'Teacher\'s position: {self._position}. \n'
              f'Teacher\'s experience {self._experience}. \n')


entrant_1 = Entrant('Yurchishin', '2002.05.03', 'Geology')
student_1 = Student('Makar', '2000.09.22', 'Geology', '2')
teacher_1 = Teacher('Shevchenko', '1973.11.17', 'Geology', 'Doctor', '10')

all_persons = [entrant_1, student_1, teacher_1]

for i in all_persons:
    i.get_info()

persons_in_age_range = []
for i in all_persons:
    if i.get_age() in range(17, 23):
        persons_in_age_range.append(i.get_last_name())

print(f'Persons who are in age range 17-23 years old: {str(persons_in_age_range)[1:-1]}')