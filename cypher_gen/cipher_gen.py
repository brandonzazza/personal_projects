#!/usr/bin/env python3
"""Main Gui For Cipher Program.

Author Brandon Zazza
Notes:
- Refer to PEP-8 for standard code formatting
"""

import base64
import tkinter as tk

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Settings
# Consider loading constants from external config file
TEXT_COLOR = "gainsboro"
TEXT_FONT = "times"


# Cipher Functions
def _generate_key(passwd: str) -> bytes:
    """Generate key from passphrase.

    - Refactored as private method, added docstrings.

    TODO: move salt to external config, look at best practices.
    """
    passwd_raw = passwd.encode()
    salt = b'salt_'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=salt,
                     iterations=100000,
                     backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(passwd_raw))

    return key


def _encrypt(message: str, key: str) -> None:
    """Encrypt message with key.

    Mutates: Output_Text.

    TODO: refactor to return string, then have callback mutate Output_Text
    """
    keyphrase = _generate_key(key)
    code = message.encode()
    fernet = Fernet(keyphrase)
    encrypted = fernet.encrypt(code)
    output = (str(encrypted, 'UTF-8'))
    Output_Text.insert(tk.END, output)


def _decrypt(encoded_message: str, key: str) -> None:
    """Decrypt message with key.

    Mutates: Output_Text.

    TODO: refactor to return string, then have callback mutate Output_Text
    """
    keyphrase = _generate_key(key)
    encrypted = str.encode(encoded_message)
    fernet = Fernet(keyphrase)
    decrypted = fernet.decrypt(encrypted)
    output = (str(decrypted, 'UTF-8'))
    Output_Text.insert(tk.END, output)


# GUI Functions
root = tk.Tk()
root.title("Cipher Machine")
canvas = tk.Canvas(root, height=400, width=500)
canvas.pack()

text_section = tk.Frame(root, bg="dark grey")
text_section.place(relwidth=1, relheight=0.75)

# Title
title = tk.Label(text_section,
                 text="CIPHER MACHINE",
                 bd=2,
                 background='grey',
                 relief="groove",
                 fg=TEXT_COLOR,
                 font=(TEXT_FONT, 20))
title.place(relwidth=1, relheight=0.1)

# Text input 1
text1 = tk.Label(text_section,
                 text="Input:",
                 background='grey',
                 relief="ridge",
                 font=(TEXT_FONT, 14),
                 fg=TEXT_COLOR)
text1.place(relx=0.025, rely=0.25, relwidth=0.14, relheight=0.1)

Input_Text = tk.Text(text_section, width=20, height=3)
Input_Text.place(relx=0.2, rely=0.11, relheight=0.38, relwidth=0.79)

# Text input 2
text2 = tk.Label(text_section,
                 text="Pass:",
                 background='grey',
                 relief="ridge",
                 font=(TEXT_FONT, 14),
                 fg=TEXT_COLOR)
text2.place(relx=0.025, rely=0.5, relwidth=0.14, relheight=0.1)

password = tk.Text(text_section, width=20, height=3)
password.place(relx=0.2, rely=0.51, relheight=0.06, relwidth=0.79)

# Text input 3
text3 = tk.Label(text_section,
                 text="Output:",
                 background='grey',
                 relief="ridge",
                 font=(TEXT_FONT, 14),
                 fg=TEXT_COLOR)
text3.place(relx=0.025, rely=0.75, relwidth=0.14, relheight=0.1)

Output_Text = tk.Text(text_section, width=20, height=3)
Output_Text.place(relx=0.2, rely=0.59, relheight=0.38, relwidth=0.79)

# total Frame
frame = tk.Frame(root, bg="light grey")
frame.place(rely=0.75, relwidth=1, relheight=0.25)

# Buttons
button_encrypt = tk.Button(
    frame,
    text="Encrypt",
    bg="grey",
    bd=4,
    fg=TEXT_COLOR,
    font=(TEXT_FONT, 18),
    command=lambda: _encrypt(Input_Text.get("1.0", 'end'),
                             password.get("1.0", 'end')))
button_encrypt.place(relx=0, rely=0, relwidth=1, relheight=0.45)

button_decrypt = tk.Button(
    frame,
    text="Decrypt",
    bg="grey",
    bd=4,
    fg=TEXT_COLOR,
    font=(TEXT_FONT, 18),
    command=lambda: _decrypt(
        Input_Text.get("1.0", 'end'),
        password.get("1.0", 'end'),
    )
)
button_decrypt.place(relx=0, rely=0.5, relwidth=1, relheight=0.45)

root.mainloop()
