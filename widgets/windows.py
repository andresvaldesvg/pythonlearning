import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed')
def button_func2():
    print('hello')

#create a window
window = tk.Tk()
window.title('Main Window')
window.geometry('800x500')

#ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# ttk text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# excercise text label
ex_label = ttk.Label (master = window, text = 'My label')
ex_label.pack()
#ex_button = ttk.Button(master = window, text = 'Click here', command = button_func2)
ex_button = ttk.Button(master = window, text = 'Click here', command = lambda: print('Hello World!'))
ex_button.pack()

#ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack()

#run 
window.mainloop()