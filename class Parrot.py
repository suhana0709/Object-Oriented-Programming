#creating class
class Parrot:
    species= "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
#odject
blu = Parrot("Blu", 5)
woo = Parrot("Woo", 4)
#accessing attributes
print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))
#accessing init variables
print("{} is {} years old.".format(blu.name, blu.age))
print("{} is {} years old.".format(woo.name, woo.age))