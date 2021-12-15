# Main Gui For Cipher Program
# Author Brandon Zazza

#Gui Import
import tkinter as tk
from tkinter import * 
from tkinter.constants import RAISED

#Cipher Import
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Settings

text_color = "gainsboro"
text_font = "times"

#Cipher Functions
def key_gen(pass_raw):

    password = pass_raw.encode()  # Convert to type bytes
    salt = b'salt_'  
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) 
    return key

def encrypt(message, password):
    key = key_gen(password)
    code = message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(code)
    output = (str(encrypted, 'UTF-8'))
    Output_Text.insert(END,output)

def decrypt(encoded_message, password):
    key = key_gen(password)
    encrypted = str.encode(encoded_message)
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    output = (str(decrypted, 'UTF-8'))
    Output_Text.insert(END,output)



# Gui Functions
root = tk.Tk()
root.title("Cipher Machine")
canvas = tk.Canvas(root, height=400, width = 500)
canvas.pack()

text_section = tk.Frame(root, bg="dark grey")
text_section.place(relwidth=1, relheight =0.75)
# Title
title=Label(text_section, text="CIPHER MACHINE",bd =2, background='grey',  relief = "groove", fg = text_color, font =(text_font,20))
title.place(relwidth = 1, relheight = 0.1)

#Text input 1
text1=Label(text_section, text="Input:", background='grey',  relief = "ridge",font=(text_font,14), fg = text_color)
text1.place(relx =0.025, rely = 0.25, relwidth = 0.14, relheight = 0.1)

Input_Text = tk.Text(text_section, width=20, height=3)
Input_Text.place(relx=0.2, rely=0.11, relheight = 0.38, relwidth = 0.79)

#Text input 2
text2=Label(text_section, text="Pass:", background='grey',  relief = "ridge",font=(text_font,14), fg = text_color)
text2.place(relx =0.025, rely = 0.5, relwidth = 0.14, relheight = 0.1)

password = tk.Text(text_section, width=20, height=3)
password.place(relx=0.2, rely=0.51, relheight = 0.06, relwidth = 0.79)

#Text input 3
text3=Label(text_section, text="Output:", background='grey',  relief = "ridge",font=(text_font,14), fg = text_color)
text3.place(relx =0.025, rely = 0.75, relwidth = 0.14, relheight = 0.1)

Output_Text = tk.Text(text_section, width=20, height=3)
Output_Text.place(relx=0.2, rely=0.59, relheight = 0.38, relwidth = 0.79)

# total Frame
frame = tk.Frame(root, bg="light grey")
frame.place(rely = 0.75, relwidth=1, relheight =0.25)

# Buttons
button_encrypt = tk.Button(frame, text = "Encrypt", bg = "grey",bd=4, fg = text_color,font =(text_font,18),command=lambda: encrypt(Input_Text.get("1.0",'end'),password.get("1.0",'end')))
button_encrypt.place(relx=0,rely=0,relwidth = 1, relheight=0.45)

button_decrypt = tk.Button(frame, text = "Decrypt", bg = "grey",bd=4, fg = text_color,font =(text_font,18), command=lambda: decrypt(Input_Text.get("1.0",'end'),password.get("1.0",'end')))
button_decrypt.place(relx=0,rely=0.5,relwidth = 1, relheight=0.45)

root.mainloop()





