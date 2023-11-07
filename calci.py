

from math import *
from tkinter import *
root = Tk()
root.title("Scientific Calculator")

# button functions


def button_click(number):
    current = Calc_entry.get()
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, str(current) + str(number))


def button_clear():
    Calc_entry.delete(0, END)


def button_add():
    first_number = Calc_entry.get()
    global f_num
    global operation
    operation = "add"
    f_num = float(first_number)
    Calc_entry.delete(0, END)


def button_subtract():
    first_number = Calc_entry.get()
    global f_num
    global operation
    operation = "subtract"
    f_num = float(first_number)
    Calc_entry.delete(0, END)


def button_multiply():
    first_number = Calc_entry.get()
    global f_num
    global operation
    operation = "multiply"
    f_num = float(first_number)
    Calc_entry.delete(0, END)


def button_divide():
    first_number = Calc_entry.get()
    global f_num
    global operation
    operation = "divide"
    f_num = float(first_number)
    Calc_entry.delete(0, END)


def button_mod():
    first_number = Calc_entry.get()
    global f_num
    global operation
    operation = "mod"
    f_num = float(first_number)
    Calc_entry.delete(0, END)


def button_pi():
    global f_num
    f_num = pi
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, pi)


def button_e():
    global f_num
    f_num = e
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, e)


def button_power():
    first_number = Calc_entry.get()
    global f_num
    global operation
    operation = "power"
    f_num = float(first_number)
    Calc_entry.delete(0, END)


def button_square():
    first_number = Calc_entry.get()
    global f_num
    global operation
    operation = "square"
    f_num = float(first_number)
    Calc_entry.delete(0, END)


def button_root():
    first_number = Calc_entry.get()
    global f_num
    global operation
    operation = "root"
    f_num = float(first_number)
    Calc_entry.delete(0, END)


def button_absolute():
    first_number = Calc_entry.get()
    global f_num
    f_num = float(first_number)
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, abs(f_num))


def button_sin():
    first_number = Calc_entry.get()
    if first_number == "π":
        first_number = pi
    global f_num
    global operation
    operation = "sin"
    f_num = float(first_number)
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, f"sin({f_num})")


def button_cos():
    first_number = Calc_entry.get()
    if first_number == "π":
        first_number = pi
    global f_num
    global operation
    operation = "cos"
    f_num = float(first_number)
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, f"cos({f_num})")


def button_tan():
    first_number = Calc_entry.get()
    if first_number == "π":
        first_number = pi
    global f_num
    global operation
    operation = "tan"
    f_num = float(first_number)
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, f"tan({f_num})")


def button_cosec():
    first_number = Calc_entry.get()
    if first_number == "π":
        first_number = pi
    global f_num
    global operation
    operation = "cosec"
    f_num = float(first_number)
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, f"cosec({f_num})")


def button_sec():
    first_number = Calc_entry.get()
    if first_number == "π":
        first_number = pi
    global f_num
    global operation
    operation = "sec"
    f_num = float(first_number)
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, f"sec({f_num})")


def button_cot():
    first_number = Calc_entry.get()
    if first_number == "π":
        first_number = pi
    global f_num
    global operation
    operation = "cot"
    f_num = float(first_number)
    Calc_entry.delete(0, END)
    Calc_entry.insert(0, f"cot({f_num})")


def button_ln():
    first_number = Calc_entry.get()
    global f_num
    global operation
    operation = "ln"
    f_num = float(first_number)
    Calc_entry.delete(0, END)


def button_equals():
    if operation == "divide":
        second_number = Calc_entry.get()
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, f_num / float(second_number))

    if operation == "multiply":
        second_number = Calc_entry.get()
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, f_num * float(second_number))

    if operation == "add":
        second_number = Calc_entry.get()
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, f_num + float(second_number))

    if operation == "subtract":
        second_number = Calc_entry.get()
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, f_num - float(second_number))

    if operation == "mod":
        second_number = Calc_entry.get()
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, f_num % float(second_number))

    if operation == "power":
        second_number = Calc_entry.get()
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, f_num ** float(second_number))

    if operation == "sin":
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, sin(f_num))

    if operation == "cos":
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, cos(f_num))

    if operation == "tan":
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, tan(f_num))

    if operation == "cosec":
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, 1/sin(f_num))

    if operation == "sec":
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, 1/cos(f_num))

    if operation == "cot":
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, 1/tan(f_num))

    if operation == "square":
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, f_num ** 2)

    if operation == "root":
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, f_num**(1/2))

    if operation == "ln":
        Calc_entry.delete(0, END)
        Calc_entry.insert(0, log(f_num))


# Entries
Calc_entry = Entry(root, text="Enter here", width=78, font=(
    'Helvetica', 20, 'bold'), bg='black', fg='powder blue', bd=30, justify=RIGHT)
Calc_entry.insert(0, "0")
# Buttons
pi_button = Button(root, text="π", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                   activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_pi)  # done
e_button = Button(root, text="e", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_e)  # done
clear_button = Button(root, text="Clear", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                      activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_clear)  # done
backspace_button = Button(root, text="⌫", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                          activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'))  # done
square_button = Button(root, text="x²", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                       activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_square)  # done
absolute_button = Button(root, text="|x|", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                         activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_absolute)  # done
mod_button = Button(root, text="mod", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                    activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_mod)  # done
root_button = Button(root, text="√x", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                     activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_root)  # done
left_bracket_button = Button(root, text="(", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                             activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'))  # done
right_bracket_button = Button(root, text=")", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                              activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'))  # done
factorial_button = Button(root, text="x!", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                          activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'))  # done
ln_button = Button(root, text="ln", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                   activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'))  # done
power_button = Button(root, text="xʸ", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                      activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_power)  # done
divide_button = Button(root, text="÷", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                       activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_divide)  # done
multiply_button = Button(root, text="x", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                         activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_multiply)  # done
subtract_button = Button(root, text="-", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                         activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_subtract)  # done
add_button = Button(root, text="+", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                    activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_add)  # done
equals_button = Button(root, text="=", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                       activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_equals)  # done
button_0 = Button(root, text="0", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(0))
button_1 = Button(root, text="1", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(1))
button_2 = Button(root, text="2", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(2))
button_3 = Button(root, text="3", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(3))
button_4 = Button(root, text="4", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(4))
button_5 = Button(root, text="5", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(5))
button_6 = Button(root, text="6", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(6))
button_7 = Button(root, text="7", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(7))
button_8 = Button(root, text="8", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(8))
button_9 = Button(root, text="9", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                  activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=lambda: button_click(9))  # done
button_point = Button(root, text=".", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                      activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'))  # done
sin_button = Button(root, text="sin", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                    activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_sin)
cos_button = Button(root, text="cos", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                    activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_cos)
tan_button = Button(root, text="tan", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                    activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_tan)
cosec_button = Button(root, text="cosec", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                      activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_cosec)
sec_button = Button(root, text="sec", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                    activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_sec)
cot_button = Button(root, text="cot", height=2, width=13, bg="black", fg="powder blue", activebackground="white",
                    activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'), command=button_cot)
graph_button = Button(root, text="graph", height=2, width=13, bg="black", fg="powder blue",
                      activebackground="white", activeforeground="black", relief="sunken", bd=10, font=('Helvetica', 20, 'bold'))

Calc_entry.grid(row=0, column=0, columnspan=5)

sin_button.grid(row=1, column=0)
pi_button.grid(row=1, column=1)
absolute_button.grid(row=1, column=2)
root_button.grid(row=1, column=3)
clear_button.grid(row=1, column=4)

cos_button.grid(row=2, column=0)
mod_button.grid(row=2, column=1)
power_button.grid(row=2, column=2)
square_button.grid(row=2, column=3)
backspace_button.grid(row=2, column=4)

tan_button.grid(row=3, column=0)
left_bracket_button.grid(row=3, column=1)
right_bracket_button.grid(row=3, column=2)
factorial_button.grid(row=3, column=3)
divide_button.grid(row=3, column=4)

cosec_button.grid(row=4, column=0)
button_7.grid(row=4, column=1)
button_8.grid(row=4, column=2)
button_9.grid(row=4, column=3)
multiply_button.grid(row=4, column=4)

sec_button.grid(row=5, column=0)
button_4.grid(row=5, column=1)
button_5.grid(row=5, column=2)
button_6.grid(row=5, column=3)
add_button.grid(row=5, column=4)

cot_button.grid(row=6, column=0)
button_1.grid(row=6, column=1)
button_2.grid(row=6, column=2)
button_3.grid(row=6, column=3)
subtract_button.grid(row=6, column=4)

e_button.grid(row=7, column=0)
ln_button.grid(row=7, column=1)
button_0.grid(row=7, column=2)
button_point.grid(row=7, column=3)
equals_button.grid(row=7, column=4)


root.mainloop()
