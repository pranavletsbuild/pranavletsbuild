class NumberCheck:
    def __init__(self,num):
        self.num=num
    def check_num(self):
        if self.num>0:
            print("positive")
        elif self.num<0:
            print("Negative")
        else:
            print("Zero")
    def even_odd(self):
        if self.num%2==0:
            print("Even")
        else:
            print("Odd")
    def square(self):
        print("square ",self.num*self.num)
    def cube(self):
        print("cube ",self.num*self.num*self.num)
while True:
    try:
        num=float(input("Enter a number:"))
    except ValueError:
        print("please enter a valid input")
    else:
        checker=NumberCheck(num)
        checker.check_num()
        checker.even_odd()
        checker.square()
        checker.cube()
        break

