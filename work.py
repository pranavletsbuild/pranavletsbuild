class NumberCheck:
    def __init__(self,num):
        self.num=num
    def check_num(self):
        if self.num>0:
            print("positive")
        elif self.  num<0:
            print("Negative")
        else:
            print("Zero")
while True:
    try:
        num=float(input("Enter a number:"))
    except ValueError:
        print("please enter a valid input")
    else:
        checker=NumberCheck(num)
        checker.check_num()
        break

