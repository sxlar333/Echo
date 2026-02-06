
import os, sys, subprocess, colorama
from pystyle import Colorate, Colors
from config.util import *

colorama.init(autoreset=True)

# ━  ┃
# ┏  ┓
# ┗  ┛
# ┣  ┫  ┳  ┻  ╋


def show_banner():
    clear_screen()
    print(BANNER)
    if menu == True:
        print(MENU1)
    else:
        print(MENU2)

info = """
    name: echo vesx rework
    version: 2.3
    developer: sxlar333
    supports: linux, maybe windows
    purpose: yeah idk honestly js use it carefully
    development will be slow as im a solo dev with school others if anyone is willing to help please dm me on discord
    my discord: sxlar_.
    more info soon
"""

INFO = Colorate.Vertical(Colors.white_to_blue, info)


def command_loop():
    while True:
        user_input = input(f"""
┌──({username_pc}@{os_name})─[~/Developer]
│                      
└─$  """).strip().lower()

        if user_input == "e":
            clear_screen()
            sys.exit()

        elif user_input == "i":
            print(INFO)
            
        elif user_input == "":
            continue
        
        elif user_input == "s":
            print("Official Vesx discord server: https://discord.gg/dwte3mus4W")

        elif user_input == "st":
            if os_name == "Linux":
                subprocess.run(['./setup.sh'])
            elif os_name == "Windows":
                subprocess.run(['setup.bat'])
            else:
                print("Incompatible OS god knows how u even got this running but atp just make a setup for ur os and send it to me :P")

        elif user_input == "1":
            subprocess.run(['python', 'plugins/webhookspammer.py'])

        elif user_input == "9":
            subprocess.run(['python', 'plugins/netscanner.py'])

        elif user_input == "10":
            subprocess.run(['python', 'plugins/portscanner.py'])
        
        elif user_input == "11":
            subprocess.run(['python', 'botstuff/bot_config.py'])
        
        elif user_input == "12":
            subprocess.run(['python', 'botstuff/bot_main.py'])

        elif user_input == "c":
            clear_screen()
            print(BANNER)
            if menu1 == True:
                print(MENU1)
            else:
                print(MENU2)
        
        elif user_input == "n":
            clear_screen()
            print(BANNER)
            print(MENU2)
            menu2 = True
            menu1 = False
            
        elif user_input == "b":
            clear_screen()
            print(BANNER)
            print(MENU1)
            menu1 = True
            menu2 = False
            

        else:
            print(f"Unknown command or command not implemented yet: {user_input}")

def main():
    show_banner()

    command_loop()

if __name__ == "__main__":
    main()
