import tkinter as tk
from tkinter.constants import RAISED

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width = 500)
canvas.pack()

frame = tk.Frame(root, bg="light grey")
frame.place(relwidth=0.2, relheight =1)

tables = tk.Frame(root, bg="light grey")
tables.place(relx = 0.2,relwidth=0.8, relheight =1)

Input_Text = tk.Entry(tables, text="Testing", font= 40)
Input_Text.place(relx=0.2, rely=0.05, relheight = 0.20, relwidth = 0.78)

button_encrypt = tk.Button(frame, text = "Encrypt", bg = "grey")
button_encrypt.place(relx=0,rely=0,relwidth = 1, relheight=0.30)

button_decrypt = tk.Button(frame, text = "Decrypt", bg = "grey")
button_decrypt.place(relx=0,rely=1/3,relwidth = 1, relheight=0.30)

button_quit = tk.Button(frame, text = "Quit", bg = "grey")
button_quit.place(relx=0,rely=2/3,relwidth = 1, relheight=0.30)

root.mainloop()