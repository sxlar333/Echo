import colorama
import ctypes
import subprocess
import os
import time
import sys
import datetime
import sys
import requests
import random
import colorama
from pystyle import Colorate, Colors

ASCII_INTERFACE = """
        ▓█████  ▄████▄   ██░ ██  ▒█████      ██▒   █▓▓█████   ██████ ▒██   ██▒
        ▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒▒██▒  ██▒   ▓██░   █▒▓█   ▀ ▒██    ▒ ▒▒ █ █ ▒░
        ▒███   ▒▓█    ▄ ▒██▀▀██░▒██░  ██▒    ▓██  █▒░▒███   ░ ▓██▄   ░░  █   ░
        ▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ ▒██   ██░     ▒██ █░░▒▓█  ▄   ▒   ██▒ ░ █ █ ▒ 
        ░▒████▒▒ ▓███▀ ░░▓█▒░██▓░ ████▓▒░      ▒▀█░  ░▒████▒▒██████▒▒▒██▒ ▒██▒
        ░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▒░▒░       ░ ▐░  ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒▒ ░ ░▓ ░
         ░ ░  ░  ░  ▒    ▒ ░▒░ ░  ░ ▒ ▒░       ░ ░░   ░ ░  ░  ░▒  ░ ░░░ ░ ░░ ░      
                        """

Menu_1 = f"""
    ┏━ [ST] Setup                                                             Exit [E] ━┓
    ┣━ [I] Info                                                               Next [N] ━┫
    ┣━ [S] Server ┏━━━━━━━━━━━━━━━━┓              ┏━━━━━━━┓          ┏━━━━━━━━━━━┓      ┃
    ┗━━━┳━━━━━━━━━┫ Discord Tools  ┣━━━━━━━━━━┳━━━┫ Osint ┣━━━━━━━┳━━┫ Web Tools ┣━━━━━━┛
        ┃         ┗━━━━━━━━━━━━━━━━┛          ┃   ┗━━━━━━━┛       ┃  ┗━━━━━━━━━━━┛
        ┣━ [01] Webhook Spammer               ┣━ [06] soon        ┣━ [09] Web Scanner
        ┣━ [02] soon                          ┣━ [07] soon        ┗━ [10] Port Scanner (just use nmap bru)
        ┣━ [03] soon                          ┗━ [08] soon
        ┣━ [04] soon
        ┗━ [05] soon
"""
Menu_2 = f"""
    ┏━ [ST] Setup                  Exit [E] ━┓
    ┣━ [I] Info                    Back [B] ━┫
    ┣━ [S] Server ┏━━━━━━━━━━━━━━━━┓         ┃
    ┗━━━┳━━━━━━━━━┫ Bot Control    ┣━━━━━━━━━┛
        ┃         ┗━━━━━━━━━━━━━━━━┛               
        ┣━ [11] Configure Bot / Reconfigure Bot                                                
        ┣━ [12] Start Bot                                                 
        ┣━ [13] soon                              
        ┣━ [14] soon
        ┣━ [15] soon
        ┣━ [16] soon
        ┣━ [17] soon
        ┗━ [18] soon
"""
BANNER = Colorate.Horizontal(Colors.white_to_blue, ASCII_INTERFACE)
MENU1 = Colorate.Horizontal(Colors.white_to_blue, Menu_1)
MENU2 = Colorate.Horizontal(Colors.white_to_blue, Menu_2)

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

menu = True

username_pc = os.getlogin()
tool_path = os.path.dirname(os.path.abspath(__file__)).split("Program\\")[0].split("Program/")[0].strip()

if sys.platform.startswith("win"):
    os_name = "Windows"
elif sys.platform.startswith("linux"):
    os_name = "Linux"
else:
    os_name = "Unknown"
    
def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")

menus = [MENU1, MENU2]

def show_banner():
    clear_screen()
    print(BANNER)
    if menu == True:
        print(MENU1)
    else:
        print(MENU2)
