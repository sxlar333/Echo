import os, sys, subprocess, colorama
from pystyle import Colorate, Colors
from config.util import *
colorama.init(autoreset=True)

# ━  ┃
# ┏  ┓
# ┗  ┛
# ┣  ┫  ┳  ┻  ╋

info = f"""
    name: echo rework
    developer: sxlar333
    version: {echo_version}
    supports: linux, windows
    development will be slow as im a solo dev with school, if anyone is willing to help please dm me on discord
    my discord: sxlar_.
    pls use this ethically im not responsible for any harm caused by the users of this tool nor the tool itself
    more info soon
"""

INFO = Colorate.Vertical(Colors.white_to_blue, info)

yelp = f"""
    ==================================================
        echo framework {echo_version}
    ====== GENERAL ===================================
    -- H = Help aka shows this
    -- C = Clears the screen
    -- E = Exits the echo framework
    -- I = Shows some more info behind the project
    -- S = Shows the Devs discord server :P, JOIN!
    ====== COMMANDS ==================================
    -- whs = discord webhook spammer
    -- ws = website scanner
    -- ps = port scanner (just use nmap dawg)
"""
YELP = Colorate.Vertical(Colors.white_to_blue, yelp)

def command_loop():
    while True:
        choose_banner()
        uin = input(CMD).strip().lower()

        if uin == "e":
            clear_screen()
            sys.exit()
            
        elif uin == "h":
            print(YELP)

        elif uin == "i":
            print(INFO)
            
        elif uin == "":
            continue
        
        elif uin == "s":
            print("Our discord server: https://discord.gg/dwte3mus4W")

        elif uin == "whs":
            subprocess.run(['python', 'plugins/webhookspammer.py'])

        elif uin == "ws":
            subprocess.run(['python', 'plugins/webscanner.py'])

        elif uin == "ps":
            subprocess.run(['python', 'plugins/portscanner.py'])

        elif uin == "c":
            clear_screen()
            choose_banner()

        else:
            print(f"Unknown command or command not implemented yet: {uin}")

def main():
    show_banner()
    command_loop()

if __name__ == "__main__":
    main()
