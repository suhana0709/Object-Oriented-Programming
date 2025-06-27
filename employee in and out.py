class Employee:
    def __init__(self):
        print("Employee created")

    #calling destructor
    def __def__(self):
        print("Destructor called")

def create_object():
    print("Making object..........")
    obj = Employee()
    print("Function end.....")
    return obj

print("Calling create_object function.......")
create_object()
print("Program end.")