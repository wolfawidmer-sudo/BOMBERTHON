import os
import sys
import time
from about import banner, menu, about, play_animation

if sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')

def main():
    play_animation()
    about()
    
    while True:
        menu()
        choice = input("    |-> ")
        
        if choice == '1':
            print("    |-----------------------------------------------------------")
            print("    |-$ Call Bombing is currently in development")
            print("    |-----------------------------------------------------------")
            time.sleep(2)
            
        elif choice == '2':
            print("    |-----------------------------------------------------------")
            from sms_bomber import smsbombingwin, smsbombinglinux
            if sys.platform == 'win32':
                smsbombingwin()
            else:
                smsbombinglinux()
            print("    |-----------------------------------------------------------")
            
        elif choice == '3':
            print("    |-----------------------------------------------------------")
            from instagram_bomber import igbombingwin, igbombinglinux
            if sys.platform == 'win32':
                igbombingwin()
            else:
                igbombinglinux()
            print("    |-----------------------------------------------------------")
            
        elif choice == '4':
            print("    |-----------------------------------------------------------")
            from whatsapp_bomber import wpbombingwin, wpbombinglinux
            if sys.platform == 'win32':
                wpbombingwin()
            else:
                wpbombinglinux()
            print("    |-----------------------------------------------------------")
            
        elif choice == '5':
            print("    |-----------------------------------------------------------")
            from email_bomber import emailbombing
            emailbombing()
            print("    |-----------------------------------------------------------")
            
        elif choice == '6':
            about()
            
        elif choice.lower() == 'x':
            print("    |-$ Exiting...")
            sys.exit(0)
            
        else:
            print("    |-$ Invalid choice!")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n    |-$ Exiting...")
        sys.exit(0)