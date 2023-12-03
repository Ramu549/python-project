# importing tkinter module
from tkinter import *


# Function to convert given weight(kg) to- grams, pounds and ounces
def covert_to_kg():
    pound = float(value.get()) * 2.20462
    gram = float(value.get()) * 1000
    ounce = float(value.get()) * 35.274
    text1.delete("1.0", END)
    text1.insert(END, str(gram))

    text2.delete("1.0", END)
    text2.insert(END, str(pound))

    text3.delete("1.0", END)
    text3.insert(END, str(ounce))


converter = Tk()
converter.title("ProjectGurukul")
converter.resizable()
l0 = Label(converter, text="Enter Weight in Kg:")
l0.grid(row=0, column=0)
value = Entry(converter)
value.grid(row=0, column=1)
# creating the button widget
b = Button(converter, text="Convert", command=covert_to_kg)
b.grid(row=0, column=2)
# creating labels widget
l1 = Label(converter, text="Gram:")
l1.grid(row=1, column=0)
l2 = Label(converter, text="Pound:")
l2.grid(row=2, column=0)
l3 = Label(converter, text="Ounce:")
l3.grid(row=3, column=0)
# creating texts widget
text1 = Text(converter, width=10, height=1)
text1.grid(row=1, column=1)
text2 = Text(converter, width=10, height=1)
text2.grid(row=2, column=1)
text3 = Text(converter, width=10, height=1)
text3.grid(row=3, column=1)

converter.mainloop()
