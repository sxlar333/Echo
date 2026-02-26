#!/bin/bash

echo echo vesx multi-tool setup wizard
echo
echo this setup may require sudo privileges 
echo
echo please enter your password if prompted
echo
read -p "Press [Enter] to continue"
sudo apt update && sudo apt upgrade -y
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo pacman -Syu --noconfirm
sudo pacman -S python --noconfirm
sudo pacman -S python-pip --noconfirm
sudo dnf update && sudo dnf upgrade -y
sudo dnf install python3 -y
sudo dnf install python3-pip -y
pip install os
pip install sys
pip install colorama
pip install pystyle
pip install webbrowser
pip install requests
pip install discord
pip install beautifulsoup4
pip install rich

echo -e "\033[4;32msetup complete, do you wish to run the tool?\033[0m"
read -p "Press enter to run or ctrl+c to quit"
python3 multi-tool.py