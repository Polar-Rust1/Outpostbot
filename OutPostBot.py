import pyfiglet
import pyautogui
import time
import keyboard
from colorama import Fore, init
import os
import sys

# Initialize colorama
init(autoreset=True)

# Function to clear the screen (for a clean interface)
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/MacOS
        os.system('clear')

# Function to print the main menu
def print_main_menu():
    # Create the big "POLARS OUTPOST BOT" text with a clearer, more spaced-out font
    polars_text = pyfiglet.figlet_format("POLARS OUTPOST BOT", font="big")
    
    # Print the header with some color and extra padding for clarity
    print(Fore.GREEN + '\n' * 2 + polars_text + '\n' * 2)  # Added padding before and after
    print(Fore.YELLOW + '-' * 50)  # Longer line for separation
    print(Fore.CYAN + "1. How to Use")
    print(Fore.MAGENTA + "2. Sell Fertilizer For Scrap")
    print(Fore.BLUE + "3. Buy Metal Fragments For Scrap")
    print(Fore.RED + "4. Exit")  # New "Exit" option
    print(Fore.YELLOW + '-' * 50)  # Another separator line for the bottom

# Function to display "How to Use" instructions
def print_how_to_use():
    print(Fore.GREEN + "\nDIRECTIONS")
    print(Fore.YELLOW + "1. MAKE SURE YOUR GAME INTERFACE IS SET TO 1.0")
    print(Fore.YELLOW + "2. BE INSIDE THE SHOPS INTERFACE WHEN YOU LAUNCH THE SCRIPT")
    print(Fore.YELLOW + "HAVE FUN\n")

# Define the coordinates for fertilizer selling
fertilizer_quantity_input_x = 1731   # X coordinate for fertilizer quantity input
fertilizer_quantity_input_y = 774    # Y coordinate for fertilizer quantity input
fertilizer_button_x = 1734           # X coordinate for fertilizer "SELL" button
fertilizer_button_y = 722            # Y coordinate for fertilizer "SELL" button

# Define the coordinates for metal fragment buying
metal_quantity_input_x = 1722       # X coordinate for metal quantity input
metal_quantity_input_y = 438        # Y coordinate for metal quantity input
metal_button_x = 1730               # X coordinate for metal "BUY" button
metal_button_y = 392                # Y coordinate for metal "BUY" button

# Action delay between steps
action_delay = 1

# Function to simulate selling fertilizer
def sell_fertilizer():
    print(Fore.GREEN + "\nSelling Fertilizer for Scrap...")
    # Code to handle the process of selling fertilizer goes here
    # Example code using pyautogui to click the "SELL" button at specified coordinates
    pyautogui.click(fertilizer_quantity_input_x, fertilizer_quantity_input_y)
    pyautogui.write('100')  # Set quantity to 100
    time.sleep(action_delay)
    pyautogui.click(fertilizer_button_x, fertilizer_button_y)  # Click "SELL" button
    print(Fore.YELLOW + "Fertilizer sold!\n")

# Function to simulate buying metal fragments
def buy_metal_fragments():
    print(Fore.GREEN + "\nBuying Metal Fragments for Scrap...")
    # Code to handle the process of buying metal fragments goes here
    # Example code using pyautogui to click the "BUY" button at specified coordinates
    pyautogui.click(metal_quantity_input_x, metal_quantity_input_y)
    pyautogui.write('100')  # Set quantity to 100
    time.sleep(action_delay)
    pyautogui.click(metal_button_x, metal_button_y)  # Click "BUY" button
    print(Fore.YELLOW + "Metal fragments bought!\n")

# Main loop that handles the script's logic
def main():
    while True:
        # Clear the screen before showing the main menu (to avoid artifact display)
        clear_screen()
        # Show the main menu
        print_main_menu()
        
        # Take input and ensure the prompt is clean
        choice = input(f"{Fore.WHITE + 'Enter 1, 2, 3, or 4: '}")

        if choice == '1':
            # Show the "How to Use" instructions
            clear_screen()
            print_how_to_use()
            input(f"{Fore.WHITE + 'Press Enter to return to the main menu...'}")  # Pause to return to menu after action
        elif choice == '2':
            # Execute fertilizer selling action
            clear_screen()
            sell_fertilizer()
            input(f"{Fore.WHITE + 'Press Enter to return to the main menu...'}")  # Pause to return to menu after action
        elif choice == '3':
            # Execute metal fragment buying action
            clear_screen()
            buy_metal_fragments()
            input(f"{Fore.WHITE + 'Press Enter to return to the main menu...'}")  # Pause to return to menu after action
        elif choice == '4':
            # Exit the script
            print(Fore.GREEN + "Exiting the script. Goodbye!")
            time.sleep(1)
            sys.exit()  # Close the script
        else:
            # Invalid selection handling
            clear_screen()
            print(f"{Fore.RED + 'Invalid selection. Please enter 1, 2, 3, or 4.'}")
            input(f"{Fore.WHITE + 'Press Enter to return to the main menu...'}")  # Pause before returning to menu

# Make sure you have a call to main() in your main loop
if __name__ == "__main__":
    main()
