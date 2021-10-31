# Main Gui Forf Cipher Program
# Author Brandon Zazza

import tkinter as tk
from tkinter import * 
from tkinter.constants import RAISED

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width = 500)
canvas.pack()

text_section = tk.Frame(root, bg="light grey")
text_section.place(relwidth=1, relheight =0.75)

title=Label(text_section, text="CIPHER MACHINE", background='grey',  relief = "groove")
title.place(relwidth = 1, relheight = 0.1)

text1=Label(text_section, text="Input:", background='grey',  relief = "ridge",font=40)
text1.place(relx =0.025, rely = 0.28, relwidth = 0.11, relheight = 0.07)

text2=Label(text_section, text="Pass:", background='grey',  relief = "ridge",font=40)
text2.place(relx =0.025, rely = 0.5, relwidth = 0.11, relheight = 0.07)

text3=Label(text_section, text="Output:", background='grey',  relief = "ridge",font=40)
text3.place(relx =0.025, rely = 0.72, relwidth = 0.11, relheight = 0.07)

Input_Text = tk.Text(text_section, width=20, height=3)
Input_Text.place(relx=0.2, rely=0.11, relheight = 0.38, relwidth = 0.79)

password = tk.Text(text_section, width=20, height=3)
password.place(relx=0.2, rely=0.51, relheight = 0.05, relwidth = 0.79)

Output_Text = tk.Text(text_section, width=20, height=3)
Output_Text.place(relx=0.2, rely=0.58, relheight = 0.38, relwidth = 0.79)

frame = tk.Frame(root, bg="light grey")
frame.place(rely = 0.75, relwidth=1, relheight =0.25)

button_encrypt = tk.Button(frame, text = "Encrypt", bg = "grey")
button_encrypt.place(relx=0,rely=0,relwidth = 1, relheight=0.30)

button_decrypt = tk.Button(frame, text = "Decrypt", bg = "grey")
button_decrypt.place(relx=0,rely=1/3,relwidth = 1, relheight=0.30)

button_quit = tk.Button(frame, text = "Quit", bg = "grey")
button_quit.place(relx=0,rely=2/3,relwidth = 1, relheight=0.30)

root.mainloop()