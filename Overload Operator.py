#making class
class A:
    def __init__(self, a):
        self.a = A
    def __lt__(self, other):
        if(self.a<other.a):
            return "obj1 is leser than obj2"
        else:
            return "obj2 is greater than obj2"
    def __eq__(self, other):
        if(self.a == other.a):
            return "obj1 is equal to obj2"
        else:
            return "obj1 is not equal to obj2"
        
#objects
obj1 = A(4)
obj2 = A(3)
print(obj1<obj2)

obj3 = A(6)
obj4 = A(6)
print(obj3 == obj4)