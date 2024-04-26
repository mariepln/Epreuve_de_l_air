import os
import subprocess
from colorama import init, Fore, Style

init()

def output_script(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def run_test(test_name, command, expected):
    output = output_script(command)
    if expected in output:
        print(f"\t{test_name}: \033[32mSuccess\033[0m")
        return True
    else:
        print(f"\t{test_name}: \033[31mFailure\033[0m")
        return False

success_count = 0
failure_count = 0

tests = {
    "air00": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air00.py "Bonjour les gars"', "expected": "Bonjour\nles\ngars"},
    "air01": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air01.py "Crevette magique dans la mer des étoiles" "la"', "expected": "Crevette magique dans \n mer des étoiles"},
    "air02": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air02.py "Je" "teste" "des" "trucs" " "', "expected": "Je teste des trucs"},
    "air03": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air03.py 1 2 3 4 5 4 3 2 1', "expected": "5"},
    "air04": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air04.py "Hello milady, bien ou quoi ??"', "expected": "Helo milady, bien ou quoi ?"},
    "air05": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air05.py 1 2 3 4 5 +2', "expected": "3 4 5 6 7"},
    "air06": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air06.py “Michel” “Albert” “Thérèse” “Benoit” “t”', "expected": "Michel"},
    "air07": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air07.py 1 3 4 2', "expected": "1 2 3 4"},
    "air08": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air08.py 10 20 30 fusion 15 25 35', "expected": "10 15 20 25 30 35"},
    "air09": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air09.py Michel Albert Thérèse Benoit', "expected": "Albert, Thérèse, Benoit, Michel"},
    "air10": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air10.py "a.txt"', "expected": "Elle danse le mia"},
    "air11": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air11.py 0 5', "expected": "    0\n   000\n  00000\n 0000000\n000000000"},
    "air12": {"path": "/home/utilisateur/Bureau/EPREUVECA/EPREUVE_AIR", "command": 'python3 air12.py 1 2 3 4 5 4 3 2 1', "expected": "5"}
}

for test_name, test_data in tests.items():
    command = test_data["command"]
    expected = test_data["expected"]
    if not os.path.isfile(test_name + ".py"):
        print(f"{test_name}.py not found")
        continue
    if run_test(test_name, command, expected):
        success_count += 1
    else:
        failure_count += 1

print(Fore.GREEN + f"\nTotal success: ({success_count}/{success_count + failure_count})" + Style.RESET_ALL)
print(Fore.RED + f"Total failure: ({failure_count}/{success_count + failure_count})" + Style.RESET_ALL)