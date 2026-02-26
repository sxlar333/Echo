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
import random
from pystyle import Colorate, Colors

echo_version = "V1.8"

username_pc = os.getlogin()
tool_path = os.path.dirname(os.path.abspath(__file__)).split("Program\\")[0].split("Program/")[0].strip()

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

banner1 = fr"""
 |\__/,|   (`\
 |_ _  |.--.) )
 ( T   )     /      welcome to the echo framework {echo_version}, {username_pc}!
(((^_(((/(((_/      use H for Help
"""

banner2 = fr"""
██    ███ ███   ███████  ██████ ██   ██  ██████  
██   █   █   █  ██      ██      ██   ██ ██    ██ 
██    ██   ██   █████   ██      ███████ ██    ██ 
██      █ █     ██      ██      ██   ██ ██    ██ 
██       █      ███████  ██████ ██   ██  ██████  

echo framework {echo_version} use H for Help
"""

banner3 = fr"""
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)     OwO , New Friend, {username_pc}?
          `-    \`_`"'-     welcome to the echo framework {echo_version} use H for Help
"""

banner4 = fr"""
 _____________________
< echo framework {echo_version}>
 ---------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\        use H for Help
                ||----w |
                ||     ||
"""
BANNER1 = Colorate.Horizontal(Colors.white_to_blue, banner1)
BANNER2 = Colorate.Horizontal(Colors.white_to_blue, banner2)
BANNER3 = Colorate.Horizontal(Colors.white_to_blue, banner3)
BANNER4 = Colorate.Horizontal(Colors.white_to_blue, banner4)


def choose_banner():
    banners = [BANNER1, BANNER2, BANNER3, BANNER4]
    return random.choice(banners)

current_banner = choose_banner()

def show_banner():
    print(current_banner)

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")
    show_banner()

if sys.platform.startswith("win"):
    os_name = "Windows"
elif sys.platform.startswith("linux"):
    os_name = "Linux"
else:
    os_name = "Unknown"

cmd = f"""


┌──({username_pc}@{os_name})─[~/Echo Framework {echo_version}]
│                      
└─$  """
CMD = Colorate.Horizontal(Colors.white_to_blue, cmd)