import tkinter as tk
from tkinter import ttk


#window
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

#button
def button_func():
    print('A basic one')
    print(radio_var.get())
    
button_string = tk.StringVar(value = 'A string var')
button = ttk.Button(window, text= 'A simple one', command = button_func, textvariable = button_string)
button.pack()

#checkbutton
check_var = tk.IntVar()
check = ttk.Checkbutton(window, 
                        text = 'Check button 1',
                        command = lambda: print (check_var.get()),
                        variable = check_var,
                        onvalue = 10,
                        offvalue = 5)
check.pack()

check2 = ttk.Checkbutton(window,
                       text = 'check2',
                       command = lambda:check_var.set(5))
check2.pack()


#radio button
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, 
                         text = 'Radio 1', 
                         value = 1,
                         variable = radio_var, 
                         command = lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, 
                         text = 'Radio2', 
                         value = 2,
                         variable = radio_var)
radio2.pack()

#ex practice
def radio_func():
    print(check_bool.get())
    check_bool.set(False)
#data
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

#widgets
exercise_radio1 = ttk.Radiobutton(window, 
                        text = 'Radio A', 
                        value = 'A', 
                        command = radio_func,
                        variable = radio_string)
exercise_radio2 = ttk.Radiobutton(window, 
                        text = 'Radio B', 
                        value = 'B',
                        command = radio_func,
                        variable = radio_string)

exercise_check = ttk.Checkbutton(window,
                        text = 'exercise check',
                        variable = check_bool, 
                        command = lambda: print(radio_string.get()))

#layouts
exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack()
#run
window.mainloop()