import os
import time

def play_animation():
    """Play ASCII animation from frames file"""
    try:
        with open('frames.txt', 'r', encoding='utf-8') as f:
            frames = f.read().split('###FRAME###')
        
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.1)
    except:
        pass

def banner():
    return """
    All Bombs away Sir
          \\
           \\           Goodbye Dullsville!
                __|__  /
       .'(\\      .-.     /)'.
    +-====(*)===: " :===(o)=====-+
            \\).  '-'  .(/
                 +=
                 +=           █▄▄ █▀█ █▀▄▀█ █▄▄ █▀▀ █▀█ ▀█▀ █ █ █▀█ █▄ █
                              █▄█ █▄█ █ ▀ █ █▄█ ██▄ █▀▄  █  █▀█ █▄█ █ ▀█
                 +=
                 +=          ###########################################
                 +=          #         Ultimate Bomber Spammer         #
                             #              Version 2.0                #
                 +=          #        github.com/wolfawidmer-sudo      #
                 +=          ###########################################
    """

def menu():
    print("""
    |------------------------|
    | 1] Call Bombing        |
    | 2] SMS Bombing         |
    | 3] Instagram Bombing   |
    | 4] WhatsApp Bombing    |
    | 5] Email Bombing       |
    | 6] About               |
    | X] Exit                |
    |------------------------|""")

def about():
    print(banner())