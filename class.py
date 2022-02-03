class Student:
    def __init__(self, name, age, test1, test2, test3):
        self.name = name
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
    def testscore(self):
        testadv = self.test1 + self.test2 + self.test3/3
        return testadv

student1 = Student("john","34",45,75,85)
student2 = Student("ted","25",75,85,70)
student3 = Student("fred","22",50,78,80)
student4 = Student("george","28",75,82,80)

print(student1.age)
print(student3.testscore())






