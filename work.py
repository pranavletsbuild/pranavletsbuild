class NumberCheck:
    def check_num(self,num):
        if num>0:
            print("positive")
        elif num<0:
            print("Negative")
        else:
            print("Zero")
while True:
    try:
        num=float(input("Enter a number:"))
    except ValueError:
        print("please enter a valid input")
    else:
        checker=NumberCheck()
        checker.check_num(num)
        break

