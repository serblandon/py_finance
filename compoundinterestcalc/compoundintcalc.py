from tkinter import *
from tkinter import messagebox


# define error message for missing info
def popup_missing():
    messagebox.showerror("Error", "Missing Data in Required Fields")


# define error message for wrong data type
def popup_datatype():
    messagebox.showerror("Error", "Wrong Format in Field(s)")


# calculate the result
def calculate(amount_entry, length_entry, interest_entry, result_entry):
    # defining variables for ease of use
    try:
        amount = float(amount_entry.get())
        length = int(length_entry.get())
        interest = float(interest_entry.get())
    except:
        # elif not isinstance(amount, (float, int)) or not isinstance(length, int) or not isinstance(interest,(float, int)):
        popup_datatype()
        raise TypeError

    # handling some errors
    if not amount or not length or not interest:
        popup_missing()

    # define formula for result
    result = amount * pow((1 + (interest / 100)), length)
            #print(result)
    # modyfying result to have only 2 decimals
    result = "%.2f"%result
            #print(result)

    # write into entry box
    result_entry.insert(0, result)
    # display entry to write the result
    result_entry.place(x=150, y=400)


# reset all boxes with null values
def reset():
    pass


# main window interface
def main_window():
    root = Tk()

    root.title("Compound Interest Calculator")

    # background color
    root.config(bg="#006496")

    root.geometry("500x500")

    # Title label
    first_label = Label(root, text="Compound Interest Calculator", font=("Helvetica", 17), bg="#006496", fg="white")
    first_label.pack()

    # initial investment labelframe
    amount_lbframe = LabelFrame(root, text="Initial Investment:", font=("Helvetica", 12), bg="#008080", fg="white")
    amount_lbframe.place(x=184, y=90)
    # entry for initial invest
    amount_entry = Entry(amount_lbframe, font=("Helvetica", 10))
    amount_entry.pack()

    # length of time labelframe - years
    length_lbframe = LabelFrame(root, text="Length Of Time(Years):", font=("Helvetica", 12), bg="#008080", fg="white")
    length_lbframe.place(x=170, y=160)
    # entry for length of time
    length_entry = Entry(length_lbframe, font=("Helvetica", 10))
    length_entry.pack()

    # interest rate labelframe - percentage
    interest_lbframe = LabelFrame(root, text="Estimated Interest Rate:", font=("Helvetica", 12), bg="#008080",
                                  fg="white")
    interest_lbframe.place(x=170, y=240)
    # entry for interest rate
    interest_entry = Entry(interest_lbframe, font=("Helvetica", 10))
    interest_entry.pack()

    # entry for result
    result_entry = Entry(root, font=("Helvetica", 14), bg="#073e4c", border=0, fg="white")

    # calculate button
    calculate_button = Button(root, text="Calculate", font=("Helvetica", 14), bg="#008080", fg="white",
                              command=lambda: calculate(amount_entry, length_entry, interest_entry, result_entry))
    calculate_button.place(x=175, y=315)

    # reset button
    reset_button = Button(root, text="Reset", font=("Helvetica", 14), bg="#ff7373", fg="white")
    reset_button.place(x=280, y=315)

    # end of window
    root.mainloop()


if __name__ == '__main__':
    main_window()
