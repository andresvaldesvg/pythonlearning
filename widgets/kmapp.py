import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
   mile_input = entry_int.get()
   km_output = mile_input * 1.61
   output_string.set(km_output)
#window
window = ttk.Window(themename = 'darkly')
window.title('Converter Ml vs Km')
window.geometry('400x150')

#title
title_label = ttk.Label(master= window, text = 'Miles to Kilometers', font= 'Arial 24 italic bold')
title_label.pack()

#input field

input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable = entry_int)
button = ttk.Button(master= input_frame, text = 'Convert', command= convert)
button2 = ttk.Button(master= input_frame, text = 'Exit', command= exit)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
button2.pack(side = 'right', padx = 20)
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master= window, 
                         text = 'Output', 
                         font= 'Arial 24', 
                         textvariable = output_string)
output_label.pack(pady = 5)

#run 
window.mainloop()