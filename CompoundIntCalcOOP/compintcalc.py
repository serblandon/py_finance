from tkinter import *
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.root = Tk()

        self.root.title("Compound Interest Calculator")

        # background color
        self.root.config(bg="#006496")

        self.root.geometry("500x625")

        # Title label
        self.first_label = Label(self.root, text="Compound Interest Calculator", font=("Helvetica", 17, "bold"),
                                 bg="#006496",
                                 fg="white")
        self.first_label.pack()

        # initial investment labelframe
        self.amount_lbframe = LabelFrame(self.root, text="Initial Investment:", font=("Helvetica", 12), bg="#008080",
                                         fg="white")
        self.amount_lbframe.place(x=184, y=90)
        # entry for initial invest
        self.amount_entry = Entry(self.amount_lbframe, font=("Helvetica", 10))
        self.amount_entry.pack()

        # length of time labelframe - years
        self.length_lbframe = LabelFrame(self.root, text="Length Of Time(Years):", font=("Helvetica", 12), bg="#008080",
                                         fg="white")
        self.length_lbframe.place(x=170, y=160)
        # entry for length of time
        self.length_entry = Entry(self.length_lbframe, font=("Helvetica", 10))
        self.length_entry.pack()

        # interest rate labelframe - percentage
        self.interest_lbframe = LabelFrame(self.root, text="Estimated Interest Rate(%):", font=("Helvetica", 12),
                                           bg="#008080",
                                           fg="white")
        self.interest_lbframe.place(x=160, y=240)
        # entry for interest rate
        self.interest_entry = Entry(self.interest_lbframe, font=("Helvetica", 10))
        self.interest_entry.pack()

        # label for result message
        self.result_label_ = Label(self.root, text="The Compounded Sum Is:", font=("Helvetica", 13), bg="#073e4c",
                                   fg="white",
                                   justify=CENTER)

        # entry for result
        self.result_entry = Entry(self.root, font=("Helvetica", 14), bg="#073e4c", border=0, fg="white", justify=CENTER)

        # entry for result in each year
        self.result_year_entry = Entry(self.root, font=("Helvetica", 13), bg="#1b4d3e", border=0, fg="white",
                                       justify=CENTER)

        # calculate button
        '''self.calculate_button = Button(self.root, text="Calculate", font=("Helvetica", 14), bg="#008080", fg="white",
                                       command=lambda: calculate(self.amount_entry, self.length_entry,
                                                                 self.interest_entry, self.result_entry,
                                                                 self.root,
                                                                 self.result_year_entry, self.result_label_))
        self.calculate_button.place(x=175, y=315)'''

        # reset button
        self.reset_button = Button(self.root, text="Reset", font=("Helvetica", 14), bg="#ff7373", fg="white",
                                   command=self.reset)
        self.reset_button.place(x=280, y=315)

        # prompt double check when closing window
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # end
        self.root.mainloop()

    # reset all boxes with null values
    def reset(self):
        self.amount_entry.delete(0, END)
        self.length_entry.delete(0, END)
        self.interest_entry.delete(0, END)
        self.result_entry.delete(0, END)
        self.result_year_entry.delete(0, END)

    # def on closing function to doulecheck if u want to quit
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()


GUI()
