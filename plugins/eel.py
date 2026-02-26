import os
from eelconfigs.e_config import *

# phase 1 just start and the menu for configs etc

banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠾⠟⠃⣀⣠⡤⢤⣤⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⣁⣤⣶⣿⣿⣿⣿⣀⣠⣿⠉⣉⣁⣤⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⠶⠋⣁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠋⠁⠀⠀
⠀⠀⠀⣤⣶⠿⠋⣠⣴⣾⣿⣿⣿⣿⣿⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  E.E.L
⠀⠀⠘⡟⢁⣴⣾⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Easy Execution Loader
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠀⠚⠻⠶⠶⠶⠤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣤⣤⣤⣤⣈⣉⠙⠛⠶⣦⣄⠀⠀
⠀⠀⠀⠀⠀⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠙⠀⠀--Yours truly, sxlar
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠖⠂⣰⣿⣿⣿⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⠶⠟⠛⣉⣠⣴⣿⣿⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⣀⣤⣤⣶⡶⠶⠟⠛⢉⣉⣠⣤⣴⣶⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⣾⡏⠉⠤⠴⠶⠶⠾⠿⠿⠟⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
color_banner = Colorate.Vertical(Colors.white_to_blue, banner)

def main_menu():
    path = input("Input path to file -> ")
    
    print(color_banner)
    
def main():
    main_menu()

if __name__ == "__main__":
    main()