import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Import PIL for image handling
import ttkbootstrap as tb  # Import ttkbootstrap for enhanced styling

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(screen_var.get())

def exit_app():
    root.quit()

root = tb.Window(themename="superhero")  # Use ttkbootstrap Window with a professional theme
root.title("Calculator")

# Load and place the logo
logo_image = Image.open("C:/Users/Andres/Desktop/pythonlearning_2_15_25/myprograms/Assets/logo.jpg")
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(root, image=logo_photo, style='TLabel')
logo_label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

# Define custom styles using ttkbootstrap
style = ttk.Style(root)
style.configure('TButton', font=('Helvetica', 14), padding=10)
style.configure('TEntry', font=('Helvetica', 20), padding=10)
style.configure('TFrame', background='#ffffff')
style.configure('TLabel', font=('Helvetica', 14), background='#ffffff')

screen_var = tk.StringVar()
screen = ttk.Entry(root, textvariable=screen_var, style='TEntry')
screen.grid(row=0, column=1, columnspan=3, sticky="nsew", ipadx=8, pady=10, padx=10)

button_frame = ttk.Frame(root, style='TFrame')
button_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row = 0
col = 0
for button in buttons:
    btn = ttk.Button(button_frame, text=button, style='TButton')
    btn.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid weights for responsiveness
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)
    button_frame.grid_rowconfigure(i, weight=1)

# Add Copy and Exit buttons
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard, style='TButton')
copy_button.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

exit_button = ttk.Button(root, text="Exit", command=exit_app, style='TButton')
exit_button.grid(row=2, column=3, sticky="ew", padx=10, pady=10)

root.mainloop()