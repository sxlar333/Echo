import os, sys, subprocess, colorama
from pystyle import Colorate, Colors

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MULTI_TOOL = os.path.join(BASE_DIR, "multi-tool.py")

token = input("Enter bot token: ")

with open("tokenbot.py", "a") as f:
    f.write(f"\nBOT_TOKEN = {token!r}\n")

choice = input("Would you like to return to the tool?: ").lower

if choice == "yes":
    subprocess.run([sys.executable, MULTI_TOOL])
else:
    print("alright bro wtv js chill in the terminal ig")