from tkinter import *


def calc_miles_to_km():
    miles = float(user_input.get())
    km = round(miles * 1.609)
    converted_km.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to", font=("Arial", 24))
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 24))
km_label.grid(column=2, row=1)

converted_km = Label(text="0", font=("Arial", 24))
converted_km.grid(column=1, row=1)

user_input = Entry()
user_input.grid(column=1,row=0)

calc_button = Button(text="Calculate", font=("Arial", 24), command=calc_miles_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()
