# Εισαγωγή βιβλιοθήκης 

import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

#Κύρια Συνάρτηση
def convert():
	mile_input = entry_int.get()
	km_output = mile_input * 1.61
	output_string.set(km_output)
	
#window build
window=ttk.Window( themename = "journal")
window.title("Web Dev from Ioannina City")
window.geometry("450x300")

#Τίτλος

title_label = ttk.Label(master = window , text = "Eφαρμογή μετατροπής απο Μίλια σε Χιλιόμετρα", font= "Helvetica 10 bold")
title_label.pack()

#Εισαγωγή Δεδομένων(text to convert plus button)
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Μετάτροπή" , command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady =10)

#Εξαγωγή Δεδομένων
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text="Αποτέλεσμα:" , font="comic 10  italic" ,textvariable = output_string)
output_label.pack( pady = 10)



window.mainloop()

#END OF APP

