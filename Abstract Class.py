#importing necessary modules
from abc import ABC, abstractmethod

#create base class
class Absclass(ABC):
    #function to print a value
    def print(self, x):
        print("Passed value: ",x)

    #abstract method
    @abstractmethod
    def task(self):
        print("We are on the task function.")

#sub-class
class text_class(Absclass):
    def task(self):
        print("We are inside text_class.")

obj=text_class()
obj.task()
obj.print(200)