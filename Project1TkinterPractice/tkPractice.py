'''
    I just want to do some simple projects to refresh my python skills during the summer
    This is a weight converter from Tkinter class, found this on geekforgeek
'''



from tkinter import *
import tkinter as tk

#Create a main window
m = tk.Tk(className= "Weight App")

def setTextInput(textExample, text):
    textExample.delete("1.0", END)
    textExample.insert(END, text)

def print_weight_in_kg_entry():
    #conversion:
    try:
        gram = float(WIE_Value.get()) * 1000
        pound = float(WIE_Value.get()) * 2.2046
        ounce = float(WIE_Value.get()) * 35.274

        setTextInput(t1, gram)
        setTextInput(t2, pound)
        setTextInput(t3, ounce)


    except:
        print("Cannot convert to Float")

#add more widgets

#Create label and Entry
l1 = tk.Label(m, text = "Weight")

WIE_Value = tk.StringVar()
E1 = weightInKgEntry = tk.Entry(m, textvariable = WIE_Value)
#Create button Convert button!

b1 = tk.Button(m, text= "convert", command = print_weight_in_kg_entry)

l2 = tk.Label(m, text = "gram")
l3 = tk.Label(m, text = "pounds")
l4 = tk.Label(m, text = "Ounce")

t1 = tk.Text(m, height = 1, width = 20)
t2 = tk.Text(m, height = 1, width = 20)
t3 = tk.Text(m, height = 1, width = 20)

#Grid them all in the same place:
l1.grid(row = 0)
E1.grid(row = 0, column = 1)
b1.grid(row = 0, column = 2)
l2.grid(row = 1, column = 0)
l3.grid(row = 1, column = 1)
l4.grid(row = 1, column = 2)
t1.grid(row = 2, column = 0)
t2.grid(row = 2, column = 1)
t3.grid(row = 2, column = 2)


    

#create Button
endButton = tk.Button(m, text = "End Program", width = 25, command = m.destroy).grid(row = 3, column = 0)

m.mainloop()