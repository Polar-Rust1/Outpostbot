import pyfiglet
import pyautogui
import time
import keyboard
from colorama import Fore, init
import os
import sys

# Initialize colorama
init(autoreset=True)

# ---------------- CONFIG ----------------

# Fertilizer selling coordinates
fertilizer_quantity_input_x = 1731
fertilizer_quantity_input_y = 774
fertilizer_button_x = 1734
fertilizer_button_y = 722

# Metal fragment buying coordinates
metal_quantity_input_x = 1722
metal_quantity_input_y = 438
metal_button_x = 1730
metal_button_y = 392

# Action delay between steps
action_delay = 1

# ----------------------------------------

# Clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu
def print_main_menu():
    title = pyfiglet.figlet_format("POLARS OUTPOST BOT", font="big")
    print(Fore.GREEN + '\n' + title + '\n')
    print(Fore.YELLOW + "-" * 50)
    print(Fore.CYAN + "1. How to Use")
    print(Fore.MAGENTA + "2. Sell Fertilizer For Scrap")
    print(Fore.BLUE + "3. Buy Metal Fragments For Scrap")
    print(Fore.RED + "4. Exit")
    print(Fore.YELLOW + "-" * 50)

# How-to instructions
def print_how_to_use():
    print(Fore.GREEN + "\nDIRECTIONS")
    print(Fore.YELLOW + "1. MAKE SURE YOUR GAME INTERFACE IS SET TO 1.0")
    print(Fore.YELLOW + "2. BE INSIDE THE SHOP INTERFACE WHEN YOU LAUNCH THE SCRIPT")
    print(Fore.YELLOW + "3. PRESS 'Q' TO STOP ANY LOOP")
    print(Fore.YELLOW + "4. RUN IN BORDERLESS WINDOW FOR BEST RESULTS\n")

# Fertilizer selling loop
def sell_fertilizer():
    print(Fore.GREEN + "\n[+] Selling Fertilizer for Scrap...")
    print(Fore.RED + "[Press 'Q' to stop]\n")
    try:
        while True:
            if keyboard.is_pressed('q'):
                print(Fore.YELLOW + "\n[!] Fertilizer loop stopped.")
                break
            pyautogui.click(fertilizer_quantity_input_x, fertilizer_quantity_input_y)
            pyautogui.write('100')
            time.sleep(action_delay)
            pyautogui.click(fertilizer_button_x, fertilizer_button_y)
            time.sleep(action_delay)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted. Returning to menu...")

# Metal buying loop
def buy_metal_fragments():
    print(Fore.GREEN + "\n[+] Buying Metal Fragments for Scrap...")
    print(Fore.RED + "[Press 'Q' to stop]\n")
    try:
        while True:
            if keyboard.is_pressed('q'):
                print(Fore.YELLOW + "\n[!] Buying loop stopped.")
                break
            pyautogui.click(metal_quantity_input_x, metal_quantity_input_y)
            pyautogui.write('20')  # change this to desired amount
            time.sleep(action_delay)
            pyautogui.click(metal_button_x, metal_button_y)
            time.sleep(action_delay)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted. Returning to menu...")

# Main logic loop
def main():
    while True:
        clear_screen()
        print_main_menu()
        choice = input(Fore.WHITE + "Enter 1, 2, 3, or 4: ")

        if choice == '1':
            clear_screen()
            print_how_to_use()
            input(Fore.CYAN + "\n[Press Enter to return to the menu...]")
        elif choice == '2':
            clear_screen()
            sell_fertilizer()
        elif choice == '3':
            clear_screen()
            buy_metal_fragments()
        elif choice == '4':
            print(Fore.GREEN + "\nExiting. See you next run!")
            time.sleep(1)
            sys.exit()
        else:
            print(Fore.RED + "\nInvalid input. Try 1, 2, 3, or 4.")
            time.sleep(1)

# Safe run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Script interrupted. Goodbye!")
        sys.exit()
