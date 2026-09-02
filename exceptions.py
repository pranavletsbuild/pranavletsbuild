while True:
    try:
        n=int(input("enter the value of n"))
        break
    except ValueError:
        print("enter a valid integer")

while True:
    try:
        k=float(input("enter the value of k"))
        break
    except ValueError:
        print("enter a valid floa number")
g = n*k
print("the value of the product is",g)
