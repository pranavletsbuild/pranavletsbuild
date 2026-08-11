def main():
    x=[23,45.89,60,56,"H",3.3,45,"U","W"]
    expcase(x)

def expcase(w):
    for item in w:
        if isinstance(item, int):
            if item%2==0:
                print("the no is even",item)
            else:
                print("the no is odd",item)
        else:
            print("This is not an integer",item)

main()