import urllib.request
import smtplib
import configparser

# Load credentials from config file
config = configparser.ConfigParser()
config.read('config.ini')

from_address = config['EMAIL']['USERNAME']
to_address = config['EMAIL']['EMAIL_TO']
subject = 'IP CHANGED'
username = config['EMAIL']['USERNAME']
password = config['EMAIL']['PASSWORD']

# Get IP
our_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

print(our_ip)

def send_email(our_ip):
    # Body of email
    body_text = our_ip + ' is our IP address'
    msg= '\r\n'.join(['To: %s' % to_address,
                      'From: %s' % from_address,
                      'Subject: %s' % subject,
                      '', body_text])

    # Sending the email
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls() 
    server.login(username, password)
    server.sendmail(from_address, to_address ,msg)
    server.quit()
    print("Email sent")

# Open up text and extract the content
with open('public_ip.txt', 'rt') as last_ip:
    last_ip = last_ip.read() # Read IP

# Check if IP has changed
if last_ip == our_ip:
    print("Our IP address has not changed")
else: 
    print("We have a new IP address")
    with open('public_ip.txt', 'wt') as last_ip:
        last_ip.write(our_ip)
        print("New IP written to text file")
        send_email(our_ip)
