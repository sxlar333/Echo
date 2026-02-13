import os, sys, subprocess, colorama
from pystyle import Colorate, Colors
from config.util import *

colorama.init(autoreset=True)

# ━  ┃
# ┏  ┓
# ┗  ┛
# ┣  ┫  ┳  ┻  ╋



info = """
    name: echo rework
    developer: sxlar333
    supports: linux, maybe windows
    development will be slow as im a solo dev with school, if anyone is willing to help please dm me on discord
    my discord: sxlar_.
    more info soon
"""

INFO = Colorate.Vertical(Colors.white_to_blue, info)


def command_loop():
    while True:
        menu1 = True
        menu2 = False
        uin = input(CMD).strip().lower()

        if uin == "e":
            clear_screen()
            sys.exit()

        elif uin == "i":
            print(INFO)
            
        elif uin == "":
            continue
        
        elif uin == "s":
            print("Our discord server: https://discord.gg/dwte3mus4W")

        elif uin == "st":
            if os_name == "Linux":
                subprocess.run(['./setup.sh'])
            elif os_name == "Windows":
                subprocess.run(['setup.bat'])
            else:
                print("Incompatible OS god knows how u even got this running but atp just make a setup for ur os and send it to me :P")

        elif uin == "1":
            subprocess.run(['python', 'plugins/webhookspammer.py'])

        elif uin == "9":
            subprocess.run(['python', 'plugins/netscanner.py'])

        elif uin == "10":
            subprocess.run(['python', 'plugins/portscanner.py'])
        
        elif uin == "11":
            subprocess.run(['python', 'botstuff/bot_config.py'])
        
        elif uin == "12":
            subprocess.run(['python', 'botstuff/bot_main.py'])

        elif uin == "c":
            clear_screen()
            print(BANNER)
            if menu1 == True:
                print(MENU1)
            elif menu2 == True:
                print(MENU2)
            else:
                print("ERROR: No menu true - command_loop() - uin == c")
        
        elif uin == "n":
            clear_screen()
            print(BANNER)
            print(MENU2)
            menu2 = True
            menu1 = False
            
        elif uin == "b":
            clear_screen()
            print(BANNER)
            print(MENU1)
            menu1 = True
            menu2 = False
            

        else:
            print(f"Unknown command or command not implemented yet: {uin}")

def main():
    show_banner()

    command_loop()

if __name__ == "__main__":
    main()
