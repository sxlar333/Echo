import requests
import time
import os
import threading
import subprocess
from pystyle import Colors, Colorate, Center




def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def setTitle(title):
    print(f"\033]0;{title}\007")

def print_text_slowly(text, delay=0.1):
    lines = text.splitlines()
    for line in lines:
        print(Colorate.Horizontal(Colors.white_to_blue, line))
        time.sleep(delay)
    print()

def main():
    print_text_slowly("Returning to main menu...")

def webhookspam():
    print_text_slowly("Enter the WebHook you want to spam")
    webhook_prompt = Colorate.Horizontal(Colors.white_to_blue, "WebHook Link -> ")
    webhook = input(webhook_prompt)
    
    try:
        requests.post(webhook, json={'content': ""})
    except:
        print_text_slowly("[!] Your WebHook is invalid!")
        time.sleep(2)
        webhookspam()
    
    print_text_slowly("\nEnter the message to spam")
    message = input(Colorate.Horizontal(Colors.white_to_blue, "Message -> "))
    
    print_text_slowly("\nAmount of messages to send")
    amount = int(input(Colorate.Horizontal(Colors.white_to_blue, "Amount -> ")))
    
    def spam():
        try:
            requests.post(webhook, json={'content': message})
        except Exception as e:
            print_text_slowly(f"Error: {e}")

    for x in range(amount):
        threading.Thread(target=spam).start()
        time.sleep(0.1)  
    print_text_slowly("[!] Webhook has been correctly spammed")
    input("\nPress ENTER to exit")
    subprocess.run(['python', 'multi-tool.py'])

if __name__ == "__main__":
    webhookspam()