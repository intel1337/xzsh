import os
import array
from colorama import Fore
import keyboard
from pynput import keyboard
import subprocess



os.system('clear')
with open("user", 'r') as file_obj:
    # read first character
    first_char = file_obj.read(1)

    if not first_char:
        os.system('python3 setup.py')
    else:
        pass

with open("user", "r") as usr:
    i = usr.read()
    for z in i.splitlines():
        user = z

history = []
with open("mzshrc", "r") as cfg:
    i = cfg.read()
    for i in i.splitlines():
        os.system(i)


while True:

    inp = input(Fore.LIGHTGREEN_EX +f"{user}@mzsh:~$"+ Fore.RESET) 

    os.system(inp)

    history.append(inp)
    f = open("stdhistory", "a")
    f.write(f"{inp}\n")
    f.close()
    if inp.startswith("cd"):
        try:
            os.chdir(inp[3:])
        except FileNotFoundError:
            print(f"No such file or directory: {inp[3:]}")
    if inp == 'exit':
        break;

    if inp == "history":
        f = open("stdhistory", "r")
        print(f.read())

 
        

