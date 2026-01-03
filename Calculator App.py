from tkinter import *
from tkinter.messagebox import *

def Add():
    first = int(first_number_entry.get())
    second = int(second_number_entry.get())
    total = first + second
    showinfo("Calculator App", f"Answer: {total}")

def Subtract():
    first = int(first_number_entry.get())
    second = int(second_number_entry.get())
    total = first - second
    showinfo("Calculator App", f"Answer: {total}")

def Multiply():
    first = int(first_number_entry.get())
    second = int(second_number_entry.get())
    total = first * second
    showinfo("Calculator App", f"Answer: {total}")

def Divide():
    first = int(first_number_entry.get())
    second = int(second_number_entry.get())
    total = first / second
    showinfo("Calculator App", f"Answer: {total}")

root = Tk()
root.title("Calculator App")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="purple")

first_number_label = Label(root, text="Enter first number:", bg="purple", fg="white", font=("Arial bold", 15))
first_number_label.pack()

first_number_entry = Entry(root, font=("Arial bold", 12))
first_number_entry.pack()

second_number_label = Label(root, text="Enter second number:", bg="purple", fg="white", font=("Arial bold", 15))
second_number_label.pack()

second_number_entry = Entry(root, font=("Arial bold", 12))
second_number_entry.pack()

addition = Button(text="Add", command=Add, bg="green", fg="white", font=("Arial bold", 15))
addition.pack()

subtraction_button = Button(text="Subtract", command=Subtract, bg="green", fg="white", font=("Arial bold", 15))
subtraction_button.pack()

multiplication_button = Button(text="Multiply", command=Multiply, bg="green", fg="white", font=("Arial bold", 15))
multiplication_button.pack()

division_button = Button(text="Divide", command=Divide, bg="green", fg="white", font=("Arial bold", 15))
division_button.pack()

root.mainloop()