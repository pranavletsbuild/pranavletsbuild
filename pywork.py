import sys

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
         print("Hello! my name is", self.name)

if len(sys.argv)<2:
    print("Please provide your name. ")
elif len(sys.argv)>2:
    print("Please provide only one name")
else:
    person = Person(sys.argv[1])
    person.greet()

