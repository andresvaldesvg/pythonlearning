import tkinter as tk
from tkinter import ttk

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

root = tk.Tk()
root.title("Calculator")

# Apply a theme
style = ttk.Style(root)
style.theme_use('clam')

screen_var = tk.StringVar()
screen = ttk.Entry(root, textvariable=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = ttk.Frame(root)
button_frame.pack()

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
    btn.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Add Copy and Exit buttons
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard, style='TButton')
copy_button.pack(side=tk.LEFT, padx=10, pady=10)

exit_button = ttk.Button(root, text="Exit", command=exit_app, style='TButton')
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()