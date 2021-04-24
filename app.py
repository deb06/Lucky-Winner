import tkinter as tk
import os
import PIL
import webbrowser
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root=tk.Tk()
root.wm_title("CONGRATULATIONS")
root.wm_maxsize(width=300, height=160)
root.wm_iconbitmap('Images/icon.ico')

def open_url():
    webbrowser.open("https://www.neighborhoodscout.com/mi/detroit/crime")

label1=tk.Label(root, text="Conratulations, you are our lucky winner!", font=("Arial", 10))
label1.grid(row=0, column=0, sticky="NW")

image1=Image.open("Images/pike.gif")
test=ImageTk.PhotoImage(image1)

label2=tk.Label(image=test)
label2.image=test
label2.grid(row=1, column=0, sticky="W")

button1=tk.Button(root, text="View Crime Statistics", font=("Arial", 10), command=open_url)
button1.grid(row=2, column=0, sticky="SW")

button2=tk.Button(root, text="Ok", font=("Arial", 10), command=root.destroy, width=8)
button2.grid(row=2, column=0, sticky="SE")

root.mainloop()