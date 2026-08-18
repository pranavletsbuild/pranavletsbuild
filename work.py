class NumberCheck:
    def check_num(self,num):
        if num>0:
            print("positive")
        elif num<0:
            print("Negative")
        else:
            print("Zero")
num=int(input("Enter a number:"))
checker=NumberCheck()
checker.check_num(num)

