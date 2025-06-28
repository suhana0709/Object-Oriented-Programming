#parent class
class Person(object):  #writing "object" is not cumpolsary
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Name: ",self.name)
        print("Idnumber: ",self.idnumber)

#child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
    
    Person.__init__(self, name, idnumber)

#object
a = Employee("Tom", "20150E05TO01", "$20k", "Intern")

a.display()