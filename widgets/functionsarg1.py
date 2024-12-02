#Topic of function with arguments inside of button
import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('a Button was pressed')
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print('a button was pressed')
        print(parameter.get())
    return inner_func



# setup
window = tk.Tk()
window.title('Buttons, functions and arguments')

#widgets
entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, 
                  textvariable = entry_string)
entry.pack()

button = ttk.Button(window, 
                    text = 'button', 
                    #Lambda function can be change to call a function
                    command = lambda: button_func(entry_string))
button.pack()

#run
window.mainloop()