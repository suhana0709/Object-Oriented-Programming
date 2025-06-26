#create a variable
class Dog:
    species = "dog"
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

bella = Dog("Golden Retriever", 4) 
frost = Dog("Siberian Husky", 5) 

print("Bella is a {}".format(bella.species))
print("Frost is a {}".format(frost.species))

print("Bella's breed is {}, and her age is {}".format(bella.breed, bella.age))
print("Frost's breed is {}, and his age is {}".format(frost.breed, frost.age))