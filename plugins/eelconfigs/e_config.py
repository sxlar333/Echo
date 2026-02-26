import os, sys, subprocess, colorama
from pystyle import Colorate, Colors
colorama.init(autoreset=True)
def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")