#making class
class Flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
      
    def __str__(self):
        
        #we will return a string
        return self.word+ ' ( '+ self.meaning+ ' )'
        
flash = []
print("*--- Welcome TO The Flashcard Application ---*")

#the following loop will be repeated until the user stops using flashcards
while True:
    word = input("\nEnter the name you want to add to your Flashcard: ")
    meaning = input("Enter the meaning of the word: ")
    
    flash.append(Flashcards(word, meaning))
    option = int(input("Enter 1 to continue, or, 2 to not: "))
    if(option==1):
        continue
    elif(option==2):
        break
    else:
        print("Only '1' or '2")
    
#printing all the flashcards
print("\n Your Flashcards :-")
for i in flash:
    print(">", i)