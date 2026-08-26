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
y=[12,3.4,56,7.8,90,"Hello",45.6,78,"World"]
k=[45,6.7,89,1.2,34,"k","l",56.7,78]
main(x)
main(y)
main(k)         