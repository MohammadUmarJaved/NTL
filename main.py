from colorama import Fore, Style,Back
import random
import pyfiglet
import kms
clo = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

print(f""" {Fore.LIGHTCYAN_EX}{pyfiglet.figlet_format("NTL",font="epic",width=100)}
{random.choice(clo)}Network Scanner  v1.0  {Style.RESET_ALL}
{Fore.YELLOW}Made By {Fore.CYAN}@MuhammadUmarFarooq{Style.RESET_ALL}                 
""")

while True:
    print("Enter the IP address or domain name: ", end="")
    inp = input(">>>  ")
    f_cms = kms.find_cms(inp)
    for key,value in f_cms.items():
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {key} {Fore.GREEN}----> {Fore.YELLOW}{value}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Done!")
    if inp == "":
        print("Please enter a valid IP address or domain name.")
        continue
    else:
        break
