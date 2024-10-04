import tkinter as tk
from tkinter import ttk

def button_func():
    #entry content
    entry_text = entry.get()

    #update label
    #label.configure(text = 'More text')
    label['text'] = entry_text

#window
window = tk.Tk()
window.title("Getting more apps")

#widgets
label = ttk.Label (master = window, text = 'My text')
label.pack()

entry = ttk.Entry (master = window)
entry.pack()

button = ttk.Button(master = window, text = "Click here", command = button_func)
button.pack()


#run
window.mainloop()