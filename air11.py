
import sys

def my_pyramid(caracter, line_nb):
    for i in range(1, line_nb + 1):
        spaces = " " * (line_nb * len(caracter) - i * len(caracter))
        print(spaces + caracter * (2 * i - 1))
    

if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

try:
    caracter = sys.argv[1]
    line_nb = int(sys.argv[2])
except ValueError:
    print("le 2éme argument doit être un entier")
    sys.exit(1)

my_pyramid(caracter, line_nb)





