from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

label_1 = Label(text="is equal to ")
label_1.grid(column=1, row=2)

label_miles = Label(text="Miles")
label_miles.grid(column=3, row=1)

label_km = Label(text="Km")
label_km.grid(column=3, row=2)

entry_miles = Entry(width=10)
entry_miles.grid(column=2, row=1)

value_km = 0
label_value_km = Label(text=value_km)
label_value_km.grid(column=2, row=2)

def calculate():
    new_value_km = int(entry_miles.get()) * 1.60934
    label_value_km.config(text=new_value_km)


button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(column=2, row=3)







window.mainloop()




