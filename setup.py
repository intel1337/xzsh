import os

os.system('clear')
os.system("pip install -r requirements.txt")
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
exit(0)
