from tkinter import *
from tkinter import messagebox


# define error message for missing info
def popup_missing():
    messagebox.showerror("Error", "Missing Data in Required Fields")


# define error message for wrong data type
def popup_datatype():
    messagebox.showerror("Error", "Wrong Format in Field(s)")


# define forward button action
def forward():



# calculate the result
def calculate(amount_entry, length_entry, interest_entry, result_entry, root, result_year_entry):
    # check if boxes are empty first
    if not amount_entry.get() or not length_entry.get() or not interest_entry.get():
        popup_missing()
    # else get variables and throw data type error if not the right format
    else:
        # defining variables for ease of use
        try:
            amount = float(amount_entry.get())
            length = int(length_entry.get())
            interest = float(interest_entry.get())
        except:
                # elif not isinstance(amount, (float, int)) or not isinstance(length, int) or not isinstance(interest,(float, int)):
            popup_datatype()
            raise TypeError
        else:
            # clear result entry box (appended results otherwise)
            result_entry.delete(0, END)

            # define formula for result
            result = amount * pow((1 + (interest / 100)), length)
            # print(result)
            # modyfying result to have only 2 decimals
            result = "%.2f" % result
            # print(result)

            # write into entry box
            result_entry.insert(0, result)
            # display entry to write the result
            result_entry.place(x=145, y=400)

            # declare list with the amount you will have each year
            list_compounded_years = []
            # loop through each year's sum and append the amount to the list
            # first element uses the initial sum formula
            year_amount = amount + (interest / 100) * amount
            list_compounded_years.append(year_amount)
            y = 1
            while y < length:
                year_amount = list_compounded_years[y - 1] + (interest / 100) * list_compounded_years[y - 1]
                list_compounded_years.append(year_amount)
                y += 1
            y = 1

            # place label to inform number of years
            years_label = Label(root, text=f"In {y} year(s) you will have", justify=CENTER, font=("Helvetica", 12),
                                bg="#1b4d3e", fg="white")
            years_label.place(x=176, y=480)
            # place result for year entry
            result_year_entry.place(x=171, y=520)
            # clear entry
            result_year_entry.delete(0, END)
            # place corresponding year there starting from 1 year
            result_year_entry.insert(0, list_compounded_years[y - 1])

            # back button to go through years
            back_button = Button(root, text="<<", fg="white", bg="#008080")
            back_button.place(x=115, y=518)

            # forward button
            forward_button = Button(root, text=">>", fg="white", bg="#008080")
            forward_button.place(x=378, y=518)

# reset all boxes with null values
def reset(amount_entry, length_entry, interest_entry, result_entry):
    amount_entry.delete(0, END)
    length_entry.delete(0, END)
    interest_entry.delete(0, END)
    result_entry.delete(0, END)


# main window interface
def main_window():
    root = Tk()

    root.title("Compound Interest Calculator")

    # background color
    root.config(bg="#006496")

    root.geometry("500x625")

    # Title label
    first_label = Label(root, text="Compound Interest Calculator", font=("Helvetica", 17, "bold"), bg="#006496",
                        fg="white")
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
    result_entry = Entry(root, font=("Helvetica", 14), bg="#073e4c", border=0, fg="white", justify=CENTER)

    # entry for result in each year
    result_year_entry = Entry(root, font=("Helvetica", 13), bg="#1b4d3e", border=0, fg="white", justify=CENTER)

    # calculate button
    calculate_button = Button(root, text="Calculate", font=("Helvetica", 14), bg="#008080", fg="white",
                              command=lambda: calculate(amount_entry, length_entry, interest_entry, result_entry, root, result_year_entry))
    calculate_button.place(x=175, y=315)

    # reset button
    reset_button = Button(root, text="Reset", font=("Helvetica", 14), bg="#ff7373", fg="white",
                          command=lambda: reset(amount_entry, length_entry, interest_entry, result_entry))
    reset_button.place(x=280, y=315)



    # end of window
    root.mainloop()


if __name__ == '__main__':
    main_window()