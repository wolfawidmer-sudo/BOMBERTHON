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

def igbombingwin():
    ig_username = input('    |-$ Your Username > ')
    ig_password = input('    |-$ Your Password > ')
    ig_victim = input("    |-$ Victim's Username > ")
    
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
    
    print('    |-$ Logging in...')
    
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
    
    browser.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)
    
    try:
        username_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = browser.find_element(By.NAME, "password")
        
        username_input.send_keys(ig_username)
        password_input.send_keys(ig_password)
        password_input.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        if "login" in browser.current_url:
            print('    |-$ Login failed')
            browser.quit()
            return
        
        print('    |-$ Logged in')
        
        try:
            not_now = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            not_now.click()
        except:
            pass
        
        try:
            not_now = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            not_now.click()
        except:
            pass
        
    except Exception as e:
        print(f'    |-$ Login error')
        browser.quit()
        return
    
    browser.get('https://www.instagram.com/direct/new/')
    time.sleep(3)
    
    try:
        search_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "queryBox"))
        )
        search_input.send_keys(ig_victim)
        time.sleep(2)
        
        user = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{ig_victim}')]"))
        )
        user.click()
        
        next_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]"))
        )
        next_btn.click()
        
        time.sleep(3)
        
        message_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )
        
        print('    |-$ Sending...')
        
        if mode == '1':
            for i in range(repcount):
                try:
                    message_input.send_keys(reptxt)
                    message_input.send_keys(Keys.ENTER)
                    time.sleep(1)
                except:
                    break
        elif mode == '2':
            for word in lyrics:
                try:
                    message_input.send_keys(word)
                    message_input.send_keys(Keys.ENTER)
                    time.sleep(1)
                except:
                    break
        
        print('    |-} Done')
        
    except Exception as e:
        print(f'    |-$ Error')
    finally:
        time.sleep(2)
        browser.quit()

def igbombinglinux():
    ig_username = input('    |-$ Your Username > ')
    ig_password = input('    |-$ Your Password > ')
    ig_victim = input("    |-$ Victim's Username > ")
    
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
    
    print('    |-$ Logging in...')
    
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
    
    browser.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)
    
    try:
        username_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = browser.find_element(By.NAME, "password")
        
        username_input.send_keys(ig_username)
        password_input.send_keys(ig_password)
        password_input.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        if "login" in browser.current_url:
            print('    |-$ Login failed')
            browser.quit()
            return
        
        print('    |-$ Logged in')
        
        try:
            not_now = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            not_now.click()
        except:
            pass
        
        try:
            not_now = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            not_now.click()
        except:
            pass
        
    except Exception as e:
        print(f'    |-$ Login error')
        browser.quit()
        return
    
    browser.get('https://www.instagram.com/direct/new/')
    time.sleep(3)
    
    try:
        search_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "queryBox"))
        )
        search_input.send_keys(ig_victim)
        time.sleep(2)
        
        user = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{ig_victim}')]"))
        )
        user.click()
        
        next_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]"))
        )
        next_btn.click()
        
        time.sleep(3)
        
        message_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )
        
        print('    |-$ Sending...')
        
        if mode == '1':
            for i in range(repcount):
                try:
                    message_input.send_keys(reptxt)
                    message_input.send_keys(Keys.ENTER)
                    time.sleep(1)
                except:
                    break
        elif mode == '2':
            for word in lyrics:
                try:
                    message_input.send_keys(word)
                    message_input.send_keys(Keys.ENTER)
                    time.sleep(1)
                except:
                    break
        
        print('    |-} Done')
        
    except Exception as e:
        print(f'    |-$ Error')
    finally:
        time.sleep(2)
        browser.quit()