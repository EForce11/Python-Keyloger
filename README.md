# Python-Keyloger

This Python program is a keylogger that records keyboard inputs. It periodically sends the recorded data as an email.

## Description

The Keylogger program allows you to monitor and record keyboard inputs on your system. It runs in the background and captures every key pressed by the user. The captured keystrokes are then stored in a log file and can be periodically sent as an email to a specified email address.

This keylogger can be used for various purposes, such as monitoring computer usage, detecting unauthorized access, or even for personal use to keep track of your own keyboard activities.

Please note that the use of this keylogger for any illegal or unethical activities is strictly prohibited. Always ensure that you have proper authorization and adhere to legal and ethical guidelines when using this program.

## Features

- Records all keyboard inputs in the background
- Periodically sends recorded data as an email
- Configurable email sending interval
- Lightweight and easy to use

## Requirements

- Python 3
- The `keyboard` library

## Usage

1. Modify the `LOG_FILE` variable with the desired log file name, if desired.
2. Replace the `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `SEND_TO_EMAIL` variables with your email account information.
3. Optionally adjust the `EMAIL_INTERVAL` variable to set the email sending interval in seconds.
4. Run the program using Python.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
