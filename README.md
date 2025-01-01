# Python-Keylogger

A lightweight keylogger for educational purposes with enhanced security and configurability.

## Features
- **Keyboard Logging**: Captures all keystrokes in the background.
- **Encrypted Logs**: Key logs are encrypted using the Fernet encryption algorithm.
- **Secure Email Sending**: Logs are periodically sent to your email securely over TLS.
- **Dynamic Configuration**: Easily configure email credentials, encryption key, and sending intervals via environment variables.
- **Cross-Platform Support**: Compatible with Windows, macOS, and Linux.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/EForce11/Python-Keyloger.git
   cd Python-Keyloger
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - `KEYLOGGER_EMAIL`: Your email address (for sending logs).
   - `KEYLOGGER_PASSWORD`: Your email password or app-specific password.
   - `KEYLOGGER_ENCRYPTION_KEY` (optional): A 32-byte key for Fernet encryption. If not set, a key will be generated.

   Example on Linux/Mac:
   ```bash
   export KEYLOGGER_EMAIL="your-email@example.com"
   export KEYLOGGER_PASSWORD="your-email-password"
   export KEYLOGGER_ENCRYPTION_KEY="32-byte-random-key"
   ```

   Example on Windows (Command Prompt):
   ```cmd
   set KEYLOGGER_EMAIL=your-email@example.com
   set KEYLOGGER_PASSWORD=your-email-password
   set KEYLOGGER_ENCRYPTION_KEY=32-byte-random-key
   ```

4. Run the keylogger:
   ```bash
   python keylogger.py
   ```

## Warning
This project is for educational purposes only. Unauthorized use of this software may violate privacy laws and result in legal consequences. Always ensure you have explicit consent from the system owner before running this program.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
