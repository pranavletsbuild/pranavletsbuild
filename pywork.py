import sys

def greet(name):
    print("Hello! my name is", name)

if len(sys.argv)<2:
    print("Please provide your name. ")
elif len(sys.argv)>2:
    print("Please provide only one name")
else:
    greet(sys.argv[1])


