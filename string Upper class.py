class IOString():
        #constructor to set default value  
    def __init__(self):
        self.str1 = ""  

        #function to get input from the user
    def getString(self):
        self.string = input("Enter string: ")
    
        # function to print the input in uppercase
    def printString(self):
        print("The string in upper case: ", self.string.upper())

#object creation
string = IOString()

#calling functions
string.getString()
string.printString()