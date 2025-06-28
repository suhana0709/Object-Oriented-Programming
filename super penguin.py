#parent class
class Bird:
    def __init__(self):
        print("Chirp Chirp!!")

    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("Swim faster!")

#child class
class Penguin(Bird):
    def __init__(self):
       super().__init__()
       print("Penguin is ready.")
       
    def whoisthis(self):
        print("Penguin")

    def run(self):
        print("Run faster!")

#object
becky = Penguin()
becky.whoisthis()
becky.swim()
becky.run()