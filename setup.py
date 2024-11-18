import os
import platform

os.system('clear')
os.system("pip install -r requirements.txt")

if platform.system() == "Linux":
    os.system('sudo apt install fastfetch')
elif platform.system() == "Darwin":
    os.system('brew install fastfetch')
inp = input("Enter your username: ")
with open("user", "a") as usr:
    usr.write(inp)
os.system('clear')
inp = input("Do you want to setup your config file ? (y/n): ")
if inp == "y":
    inp = input("Enter your config: ")
    with open("config", "w") as cfg:
        cfg.write(inp)
        os.system('clear')
        print("Config file created successfully.")
        cfg.close()
else:
    os.system('clear')
    print("Config file not created.")
    input("Press enter to exit...")
    os.system('python3 main.py')
exit(0)
