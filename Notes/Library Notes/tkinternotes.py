import tkinter as tk
from tkinter import Canvas, Tk

root = tk.Tk()

Window = Tk()

canvas = Canvas(Window, width=100, height=100)

canvas.create_rectangle(20, 40, 20, 40)

button = tk.Button(root, text="click me")

button.pack()

def on_button_click():
    print("button clicked")
button.bind("<Button-1>", on_button_click)

btn = tk.Label()
text = tk.Text("insert text", width=10, height=10, font="Ariel")

from tkinter import messagebox

tk.textbox.get("1.0", tk.END)

root.mainloop()