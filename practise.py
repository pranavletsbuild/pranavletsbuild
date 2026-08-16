def main(x):
    obj=numcheck(x)
    obj.process()
class numcheck:
    def __init__(self,numbers):
        self.numbers=numbers

    def process(self):
        for item in self.numbers:
            if isinstance(item, int):
                if item%2==0:
                    print("the no is even",item)
                else:
                    print("the no is odd",item)
            else:
                print("This is not an integer",item)

x=[23,45.89,60,56,"H",3.3,45,"U","W"]
main(x)