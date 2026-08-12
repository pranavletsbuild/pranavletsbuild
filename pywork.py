import sys

if len(sys.argv)<2:
    print("less no of arguments not allowed ")
elif len(sys.argv)>2:
    print("more no of arguments not allowed")
else:
    print("Hello! my name is",sys.argv[1])


