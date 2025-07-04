#class creation
class myClass:
    #private variable
    __privateVar = 27;
    
    def __privMeth(self):
        print("I am doing my coding class.")

    #function for printing the private value
    def hello(self):
        print("Private Value: ", myClass.__privateVar)

#creating object for displaying values
foo = myClass()
foo.hello()
foo.__privMeth()