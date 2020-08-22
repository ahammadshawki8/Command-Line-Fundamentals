# argparse module
# argparse stands for arguement parser

# in this module, we will learn argparse module for making CLI(command line interface).
# why should we make CLI?
# it is helpful for interecting our own programme,
# little easier for calling methods from command line,
# change variable and perform other tasks quickier by command line
# instead of opening the file and edit it.
# CLI is also useful anytime we will setup something.

# here we have a basic function
def calc(x, y, operation):
    if operation == "add":
        return x+y
    elif operation == "sub":
        return x-y
    elif operation == "mul":
        return x*y
    elif operation == "div":
        return x/y


# we will convert this into a command line interface using argparse.
# we need to import argparse and sys
import argparse
import sys

# then we will define a main() function when we will define the arguements.
def main():
    # here we have to define the parser
    # we can do that by ArguementParser() method
    parser = argparse.ArgumentParser()
    # here ArgumentParser is a class and parser is an object of that class.

    # now we have to add arguement in the parser by add_arguement() method
    parser.add_argument("--x", type = float, default=1.0, help="What is the first number?")
    # --x will take place of the x parameter
    # we have to set the type using type arguement
    # we also have  default and help arguement
    # default arguement is the default value and help arguement is a string which is used for description.
    
    parser.add_argument("--y", type = float, default=1.0, help="What is the second number?")
    parser.add_argument("--operation", type = str, default="add", help="What operation? (add,sub,mul,div)" )

    # now we have parse the arguements and save them in a variable.
    # we can do this by parse_args() function.
    args = parser.parse_args()

    # and then we will need to write the return value as standard output in console.
    # we can do that by sys.stdout.write() function.
    sys.stdout.write(str(calc2(args)))
    # here we have to print the string version of the return value.


# Now we have to change the calc function that we previously defined.
def calc2(args):                 # here we need only args arguement
    # and we have to write args. infront of every arguement.
    if args.operation == "add":
        return args.x+args.y
    elif args.operation == "sub":
        return args.x-args.y
    elif args.operation == "mul":
        return args.x*args.y
    elif args.operation == "div":
        return args.x/args.y

# Now we have to use "__main__"
if __name__ == "__main__":
    main()

# Now we need to save our file and pull up command window.
# we have to write this command in the command line:
"""python "13. Command Line/4. Argparse module of python.py" """
# we can change the variables by adding --x=value --y=value --operation=value
""" python "13. Command Line/4. Argparse module of python.py" --x=10 --y=2 --operation=div"""
# for help output we can use -h
"""python "13. Command Line/4. Argparse module of python.py" -h"""