
class Reverse:
    def __init__(self, word):
        self.word = word
        rev = self.word[::-1]
        print("Reversed form: ",rev)
    

b = input("Enter something that is to be reversed: ")
a = Reverse(b)