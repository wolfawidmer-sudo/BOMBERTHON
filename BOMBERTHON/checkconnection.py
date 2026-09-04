import socket

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def check():
    print("    |-$ Checking connection...")
    if check_internet():
        print("    |-$ Connected")
        return True
    else:
        print("    |-$ No connection")
        return False