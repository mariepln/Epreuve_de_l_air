import sys
import error_handling

def my_pyramid(caracter, line_nb):
    for i in range(1, line_nb + 1):
        spaces = " " * (line_nb * len(caracter) - i * len(caracter))
        print(spaces + caracter * (2 * i - 1))
    
error_handling.check_arguments_less_than_2()

caracter = sys.argv[1]
try:
    line_nb = int(sys.argv[2])
except ValueError:
    print("error")
    sys.exit(1)

my_pyramid(caracter, line_nb)





