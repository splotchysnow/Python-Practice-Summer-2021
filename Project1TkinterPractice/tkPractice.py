import tkinter as tk


    

#Create a main window
m = tk.Tk(className= "Weight App")

def setTextInput(textExample, text):
    textExample.delete(1.0,"end")
    textExample.insert(1.0, text)

def print_weight_in_kg_entry():
    #conversion:
    try:
        gram = float(WIE_Value.get()) * 1000
        pound = float(WIE_Value.get()) * 2.2046
        ounce = float(WIE_Value.get()) * 35.274

        setTextInput(t1, str(gram))
        setTextInput(t2, str(pound))
        setTextInput(t3, str(ounce))
        


    except:
        print("Cannot convert to Float")

#add more widgets

#Create label and Entry
tk.Label(m, text = "Weight").grid(row = 0)

WIE_Value = tk.StringVar()
weightInKgEntry = tk.Entry(m, textvariable = WIE_Value).grid(row = 0, column = 1)
#Create button Convert button!

tk.Button(m, text= "convert", command = print_weight_in_kg_entry).grid(row = 0, column = 2)

tk.Label(m, text = "gram").grid(row = 1, column = 0)
tk.Label(m, text = "pounds").grid(row = 1, column = 1)
tk.Label(m, text = "Ounce").grid(row = 1, column = 2)

t1 = tk.Text(m, height = 1, width = 20).grid(row = 2, column = 0)
t2 = tk.Text(m, height = 1, width = 20).grid(row = 2, column = 1)
t3 = tk.Text(m, height = 1, width = 20).grid(row = 2, column = 2)



    

#create Button
endButton = tk.Button(m, text = "End Program", width = 25, command = m.destroy).grid(row = 3, column = 0)

m.mainloop()