class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, year, faculty):
        super().__init__(name, age)
        self.year = year
        self.faculty = faculty

    # def show_info(self):
    #     print(self.name, self.age, self.year, self.faculty)

s1 = Student("Mike", 21, 3, "IT")
s1.show_info()
# print(s1.name)
