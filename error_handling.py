import sys

def check_arguments_less_than_2():
    if len(sys.argv) < 3:
        print("arguments error")
        sys.exit(1)

def check_arguments_less_than_1():
    if len(sys.argv) < 2:
        print("arguments error")
        sys.exit(1)

def check_arguments_less_than_3():
    if len(sys.argv) < 4:
        print("arguments error")
        sys.exit(1)

def check_arguments_greather_than_2():
    if len(sys.argv) > 3:
        print("arguments error")
        sys.exit(1)

def check_arguments_greather_than_1():
    if len(sys.argv) > 2:
        print("arguments error")
        sys.exit(1)

def check_number_only(arguments):
    for argument in arguments:
        try:
            int(argument)
        except ValueError:
            print("error: no integer arg")
            sys.exit(1)