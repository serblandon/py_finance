from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt


class GUI:
    def __init__(self):

        self.root = Tk()
        # initialize variables which are used in multiple methods and modified in calculate method
        self.list_compounded_years = None
        self.amount = None
        self.length = None
        self.interest = None
        self.result_label_ = None
        self.years_label = None
        self.nocompound_years = None

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

        # entry for result
        self.result_entry = Entry(self.root, font=("Helvetica", 14), bg="#073e4c", border=0, fg="white", justify=CENTER)

        # entry for result in each year
        self.result_year_entry = Entry(self.root, font=("Helvetica", 13), bg="#1b4d3e", border=0, fg="white",
                                       justify=CENTER)

        # calculate button
        self.calculate_button = Button(self.root, text="Calculate", font=("Helvetica", 14), bg="#008080", fg="white",
                                       command=self.calculate)
        self.calculate_button.place(x=175, y=315)

        # reset button
        self.reset_button = Button(self.root, text="Reset", font=("Helvetica", 14), bg="#ff7373", fg="white",
                                   command=self.reset)
        self.reset_button.place(x=280, y=315)

        # back button to go through years
        self.back_button = Button(self.root, text="<<", fg="white", bg="#008080",
                                  command=lambda: self.back(2))

        # forward button
        self.forward_button = Button(self.root, text=">>", fg="white", bg="#008080",
                                     command=lambda: self.forward(2))

        # button for plotting
        self.plotting_button = Button(self.root, text="Plot", font=("Helvetica", 13), fg="white", bg="#008080",
                                      command=self.plot)

        # prompt double check when closing window
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # end
        self.root.mainloop()

    # def on closing function to doulecheck if u want to quit
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
            plt.close()

    # define error message for missing info
    @staticmethod
    def popup_missing():
        messagebox.showerror("Error", "Missing Data in Required Fields")

    # define error message for wrong data type
    @staticmethod
    def popup_datatype():
        messagebox.showerror("Error", "Wrong Format in Field(s)")

    # reset all entities with null values
    def reset(self):
        self.amount_entry.delete(0, END)
        self.length_entry.delete(0, END)
        self.interest_entry.delete(0, END)
        self.result_entry.delete(0, END)
        self.result_year_entry.delete(0, END)
        self.result_label_.destroy()
        self.years_label.destroy()
        plt.close()

    # def method to build the list for compounded value for each year
    def build_list(self):
        # declare list with the amount you will have each year
        self.list_compounded_years = []
        # loop through each year's sum and append the amount to the list
        # first element uses the initial sum formula
        year_amount = self.amount + (self.interest / 100) * self.amount
        self.list_compounded_years.append(year_amount)
        y = 1
        while y < self.length:
            year_amount = self.list_compounded_years[y - 1] + (
                    (self.interest / 100) * self.list_compounded_years[y - 1])
            self.list_compounded_years.append(year_amount)
            y += 1

    # build list for another line in plot without compounding
    def build_wo_comp(self):
        # initialize list
        self.nocompound_years = []
        # add initial sum
        self.nocompound_years.insert(0, self.amount)
        # loop through each year's sum and append the amount to the list
        # first element uses the initial sum formula
        year_amount = self.amount + (self.interest / 100) * self.amount
        self.nocompound_years.append(year_amount)
        y = 2
        while y < self.length + 1:
            year_amount += (self.interest / 100) * self.amount
            self.nocompound_years.append(year_amount)
            y += 1

    # calculate the result
    def calculate(self):
        # check if boxes are empty first
        if not self.amount_entry.get() or not self.length_entry.get() or not self.interest_entry.get():
            GUI.popup_missing()
        # else get variables and throw data type error if not the right format
        else:
            # defining variables for ease of use
            try:
                self.amount = float(self.amount_entry.get())
                self.length = int(self.length_entry.get())
                self.interest = float(self.interest_entry.get())
            except:
                GUI.popup_datatype()
                raise TypeError
            else:
                # clear result entry box (appended results otherwise)
                self.result_entry.delete(0, END)

                # define formula for result
                result = self.amount * pow((1 + (self.interest / 100)), self.length)
                # print(result)
                # modifying result to have only 2 decimals
                result = "%.2f" % result
                # print(result)

                # label for result message
                self.result_label_ = Label(self.root, text="The Compounded Sum Is:", font=("Helvetica", 13),
                                           bg="#073e4c",
                                           fg="white",
                                           justify=CENTER)

                # label for result
                self.result_label_.place(x=155, y=370)

                # write into entry box
                self.result_entry.insert(0, result)
                # display entry to write the result
                self.result_entry.place(x=145, y=400)

                # call the method to build the list for each year
                self.build_list()

                # call method to build uncompounded list
                self.build_wo_comp()

                # place label to inform number of years
                self.years_label = Label(self.root, text=f"In {1} year you will have....", justify=CENTER,
                                         font=("Helvetica", 12),
                                         bg="#1b4d3e", fg="white")
                self.years_label.place(x=173, y=480)

                # place result for year entry
                self.result_year_entry.place(x=168, y=520)
                # clear entry
                self.result_year_entry.delete(0, END)
                # place corresponding year there starting from 1 year
                self.result_year_entry.insert(0, "%.2f" % self.list_compounded_years[0])

                self.back_button.place(x=115, y=518)

                self.forward_button.place(x=378, y=518)

                self.plotting_button.place(x=240, y=570)

                # close plot when clicking calculate with new values
                plt.close()

    # define back button action
    def back(self, y):
        self.result_year_entry.delete(0, END)
        self.years_label = Label(self.root, text=f"In {y} year(s) you will have", justify=CENTER,
                                 font=("Helvetica", 12),
                                 bg="#1b4d3e", fg="white")
        # redefine forward/back buttons
        self.forward_button = Button(self.root, text=">>", fg="white", bg="#008080",
                                     command=lambda: self.forward(y + 1))
        self.back_button = Button(self.root, text="<<", fg="white", bg="#008080",
                                  command=lambda: self.back(y - 1))
        # check if it is out of range
        if y == 1:
            self.back_button = Button(self.root, text="<<", state=DISABLED, fg="white", bg="#008080")
        # place button overwritten
        else:
            self.back_button.place(x=115, y=518)
        # place button overwritten
        self.forward_button.place(x=378, y=518)

        self.years_label.place(x=176, y=480)
        self.result_year_entry.insert(0, "%.2f" % self.list_compounded_years[y - 1])

    # define forward button action
    def forward(self, y):
        self.result_year_entry.delete(0, END)
        self.years_label = Label(self.root, text=f"In {y} year(s) you will have", justify=CENTER,
                                 font=("Helvetica", 12),
                                 bg="#1b4d3e", fg="white")
        # redefine forward/back buttons
        self.forward_button = Button(self.root, text=">>", fg="white", bg="#008080",
                                     command=lambda: self.forward(y + 1))
        # redefine back button
        self.back_button = Button(self.root, text="<<", fg="white", bg="#008080",
                                  command=lambda: self.back(y - 1))
        # check if it is out of range
        if y == len(self.list_compounded_years):
            self.forward_button = Button(self.root, text=">>", state=DISABLED, fg="white", bg="#008080")
        # place button overwritten
        else:
            self.forward_button.place(x=378, y=518)
        # place button overwritten
        self.back_button.place(x=115, y=518)

        self.years_label.place(x=176, y=480)
        self.result_year_entry.insert(0, "%.2f" % self.list_compounded_years[y - 1])

    # def plot method
    def plot(self):
        # make a copy from the initial list so that it doesn't spoil the arrow iteration through the values
        # add initial amount to the list to start from the same point
        list_compounded_years_cpy = self.list_compounded_years.copy()
        list_compounded_years_cpy.insert(0, self.amount)
        # plot uncompounded list
        plt.plot(self.nocompound_years, label="Sum with no compound")
        # plot compounded list
        plt.plot(list_compounded_years_cpy, label="Compounded sum")
        # create a list for the flat line representing initial sum through the years
        list_same_value = [self.amount for element in list_compounded_years_cpy]
        plt.plot(list_same_value, label="Initial sum")
        plt.title("Your initial sum compounded")
        plt.xlabel("$Years$")
        plt.ylabel("$Amount$")
        plt.legend(loc="upper left")
        plt.show()


GUI()
