#creating class
class Convert:
    def __init__(self):
        while True:
           try:
               print("\n Number Range: 1-3999")
               self.num = int(input("Enter the number: "))
               if 1<= self.num <=3999:
                   break
                   print("Out of range, try again!")
           except ValueError:
                print("Enter a number please!")
      # a method for the conversion
    def convert(self):
        table = [ 
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10,"X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
            ]

        result = ''
        num = self.num
        for value, symbol in table:
            while num>=value:
                result += symbol
                num -= value
        return result

print("*--- Integer to Roman Converter ---*")

#making object
a = Convert()
print(a.convert())