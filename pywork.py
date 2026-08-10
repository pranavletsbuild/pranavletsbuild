import sys

try:
    print("Hi my name is:", sys.argv[1])
except IndexError:
    print("Please provide your name as a command-line argument.")
