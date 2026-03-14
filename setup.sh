#!/usr/bin/env bash

set -e

clear

# yes this setup script was ai generated but i honestly cant be asked to learn more bash at 2 am sorry guys

echo "===================================="
echo "        ECHO FRAMEWORK SETUP        "
echo "===================================="
echo
echo "This wizard will install the required dependencies."
echo "You may be asked for your sudo password."
echo

read -p "Press [Enter] to begin..."

# Detect distro
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo "Unable to detect Linux distribution."
    exit 1
fi

echo
echo "Detected distro: $DISTRO"
echo

install_debian() {
    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y python3 python3-pip
}

install_arch() {
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm python python-pip
}

install_fedora() {
    sudo dnf upgrade -y
    sudo dnf install -y python3 python3-pip
}

install_alpine() {
    sudo apk update
    sudo apk add python3 py3-pip
}

install_opensuse() {
    sudo zypper refresh
    sudo zypper install -y python3 python3-pip
}

# Choose install function
case "$DISTRO" in
    ubuntu|debian|linuxmint|pop)
        install_debian
        ;;
    arch|manjaro|endeavouros)
        install_arch
        ;;
    fedora)
        install_fedora
        ;;
    alpine)
        install_alpine
        ;;
    opensuse*|suse)
        install_opensuse
        ;;
    *)
        echo "Unsupported distro: $DISTRO"
        echo "Please install Python3 and pip manually."
        exit 1
        ;;
esac

echo
echo "Installing Python dependencies..."

pip3 install --upgrade pip

pip3 install \
colorama \
pystyle \
requests \
discord \
beautifulsoup4 \
rich

echo
echo "===================================="
echo " Setup complete!"
echo "===================================="
echo

read -p "Press [Enter] to run the tool or CTRL+C to exit..."

python3 multi-tool.py