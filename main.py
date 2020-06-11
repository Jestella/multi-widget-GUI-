from tkinter import *

# Create an empty Tkinter window
window=Tk()

# Get user value from input box and mutiply to get kilograms, pounds, and ounces
def from_kg():
  grams=float(a2_value.get())*1000
  pounds=float(a2_value.get())*2.20462
  ounces=float(a2_value.get())*35.274

# Empty the Text boxes if they had text from the previous use and fill them again
# Deletes the content of the Text box from start to END
  t1.delete("1.0",END) 
# Fill in the text box with the value of gram Variable
  t1.insert(END, grams) 
  t2.delete("1.0",END) 
  t2.insert(END, pounds)
  t3.delete("1.0",END) 
  t3.insert(END, ounces)

# Create a label widget with "Kg" as label
a1=Label(window,text="Kg")
a1.grid(row=0,column=0)

# Create a special StringVar object
a2_value=StringVar()
# Create an Entry box for users to enter the value
a2=Entry(window,textvariable=a2_value)
a2.grid(row=0,column=1)

# Create a button Widget
# The from_kg() function is called when the button is pushed
b1=Button(window,text="Convert", command=from_kg)
b1.grid(row=0,column=2)

# Create three empty text boxes, t1, t2, and t3
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

# This makes sure to keep the main window open
window.mainloop()