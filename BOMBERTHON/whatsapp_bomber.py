from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import time
import os

def wpbombingwin():
    print("    |-$ Starting WhatsApp Web...")
    print("    |-$ Scan the QR code with your phone")
    
    options = ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe')
    
    if not os.path.exists(chromedriver_path):
        print(f'    |-$ ChromeDriver not found')
        return
    
    service = ChromeService(executable_path=chromedriver_path)
    
    try:
        browser = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f'    |-$ Failed to start Chrome')
        return
    
    browser.get('https://web.whatsapp.com/')
    
    try:
        WebDriverWait(browser, 600).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='chat-list-search']"))
        )
        print("    |-$ Logged in")
    except:
        print("    |-$ Timeout")
        browser.quit()
        return
    
    wp_victim = input("    |-$ Victim's Phone Number (with country code) > ")
    bad_chars = ['+', ' ', '-']
    
    for i in bad_chars:
        wp_victim = wp_victim.replace(i, '')
    
    mode = input('''    |
    |------------------------|
    | 1] Repetitive Mode     |
    | 2] Script/Lyrical Mode |
    |------------------------|
    |-> ''')
    
    if mode == '1':
        reptxt = input('    |-$ Message > ')
        try:
            repcount = int(input('    |-$ How many times ? > '))
        except ValueError:
            print('    |-$ Invalid number')
            return
    elif mode == '2':
        try:
            with open("lyrics.txt", "r") as f:
                lyrics = f.read().split()
        except FileNotFoundError:
            print('    |-$ lyrics.txt not found')
            return
    else:
        print('    |-$ Invalid choice')
        return
    
    browser.get(f'https://web.whatsapp.com/send?phone={wp_victim}')
    
    try:
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='conversation-panel-wrapper']"))
        )
    except:
        print("    |-$ Could not open chat")
        browser.quit()
        return
    
    try:
        input_box = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='conversation-compose-box-input']"))
        )
    except:
        try:
            input_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
        except:
            print("    |-$ Could not find input")
            browser.quit()
            return
    
    print("    |-$ Sending...")
    
    if mode == '1':
        for i in range(repcount):
            try:
                input_box.send_keys(reptxt)
                input_box.send_keys(Keys.ENTER)
                time.sleep(0.5)
            except:
                break
    elif mode == '2':
        for word in lyrics:
            try:
                input_box.send_keys(word)
                input_box.send_keys(Keys.ENTER)
                time.sleep(0.5)
            except:
                break
    
    print('    |-} Done')
    time.sleep(2)
    browser.quit()

def wpbombinglinux():
    print("    |-$ Starting WhatsApp Web...")
    print("    |-$ Scan the QR code with your phone")
    
    options = FirefoxOptions()
    options.add_argument("--log-level=3")
    
    geckodriver_path = os.path.join(os.getcwd(), 'geckodriver')
    
    if not os.path.exists(geckodriver_path):
        print(f'    |-$ GeckoDriver not found')
        return
    
    service = FirefoxService(executable_path=geckodriver_path)
    
    try:
        browser = webdriver.Firefox(service=service, options=options)
    except Exception as e:
        print(f'    |-$ Failed to start Firefox')
        return
    
    browser.get('https://web.whatsapp.com/')
    
    try:
        WebDriverWait(browser, 600).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='chat-list-search']"))
        )
        print("    |-$ Logged in")
    except:
        print("    |-$ Timeout")
        browser.quit()
        return
    
    wp_victim = input("    |-$ Victim's Phone Number (with country code) > ")
    bad_chars = ['+', ' ', '-']
    
    for i in bad_chars:
        wp_victim = wp_victim.replace(i, '')
    
    mode = input('''    |
    |------------------------|
    | 1] Repetitive Mode     |
    | 2] Script/Lyrical Mode |
    |------------------------|
    |-> ''')
    
    if mode == '1':
        reptxt = input('    |-$ Message > ')
        try:
            repcount = int(input('    |-$ How many times ? > '))
        except ValueError:
            print('    |-$ Invalid number')
            return
    elif mode == '2':
        try:
            with open("lyrics.txt", "r") as f:
                lyrics = f.read().split()
        except FileNotFoundError:
            print('    |-$ lyrics.txt not found')
            return
    else:
        print('    |-$ Invalid choice')
        return
    
    browser.get(f'https://web.whatsapp.com/send?phone={wp_victim}')
    
    try:
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='conversation-panel-wrapper']"))
        )
    except:
        print("    |-$ Could not open chat")
        browser.quit()
        return
    
    try:
        input_box = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='conversation-compose-box-input']"))
        )
    except:
        try:
            input_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
        except:
            print("    |-$ Could not find input")
            browser.quit()
            return
    
    print("    |-$ Sending...")
    
    if mode == '1':
        for i in range(repcount):
            try:
                input_box.send_keys(reptxt)
                input_box.send_keys(Keys.ENTER)
                time.sleep(0.5)
            except:
                break
    elif mode == '2':
        for word in lyrics:
            try:
                input_box.send_keys(word)
                input_box.send_keys(Keys.ENTER)
                time.sleep(0.5)
            except:
                break
    
    print('    |-} Done')
    time.sleep(2)
    browser.quit()