# importing necessary methods
from abc import ABC, abstractmethod

#base class
class Animal(ABC):
   #abstract methods
    #should be implemeted by all sub-classes
    def move(self):
        pass


#sub-classes
class Human(Animal):
    def move(self):
        print("I can walk.")

class Snake(Animal):
    def move(self):
        print("I can crawl.")

class Dog(Animal):
    def move(self):
        print("I can bark.")

#objects
H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()