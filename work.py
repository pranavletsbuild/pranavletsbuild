def check_num(num):
    if num>0:
        print("positive")
    elif num<0:
        print("Negative")
    else:
        print("Zero")

num =int(input("Enter a number:"))
check_num(num)