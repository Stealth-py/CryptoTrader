import time
from tkinter import *
import webbrowser, config
from binanceapi import binance_interface

help_url = "https://github.com/Stealth-py/CryptoTrader"

class GUI(Tk):
    """
        This class contains all the methods to intialize a working GUI for the trading bot.
    """

    def __init__(self):
        Tk.__init__(self)

        self.title("CryptoTrader")
        self.configure(background="black")

        self.widgets()
        self.choose_api()


    def widgets(self):
        """
            Creates a 'Menu()' object named 'mainmenu'
            Adds the command 'Help' which, onclick, redirects us to the github repository of this project.
            Repository: 'https://github.com/Stealth-py/CryptoTrader'
        """

        mainmenu = Menu(self)
        mainmenu.add_command(label = "Help", underline=1, command = lambda: webbrowser.open(help_url))
        self.config(menu = mainmenu)


    def choose_api(self):
        """
            Choose an API from the options given below.
        """
        self.geometry("600x400")
        home = Frame(self)
        home.configure(background="black")
        var = IntVar(0)

        def check():
            self.apichoice = var.get()

        def call_appropriate_function():
            try:
                name = config.API_LIST[self.apichoice - 1]
                self.destroy()
                w = eval(f"{name}_interface.{name.capitalize()}API()")
                w.mainloop()
            except:
                b.grid_forget()
                l = Button(home, text = "Choose a valid option!!!!", fg = "red", command = self.choose_api)
                l.grid(row = 2, pady = 6)

        heading = Label(home, relief = "groove", text = "Choose an API from the options given below", font = ("helvetica", 10, "bold"))
        heading.grid(row = 0, sticky = "NESW", pady = 6)

        o = Radiobutton(home, text = "Binance API", variable = var, value = 1, command = check, anchor = "w")
        o.grid(row = 1, sticky = W)

        b = Button(home, text = "Next", command = lambda: [call_appropriate_function()])
        b.grid(row = 2, column = 1)

        home.grid(row = 0, column = 0, sticky = "NESW")
        home.grid_rowconfigure(0, weight = 1)
        home.grid_columnconfigure(0, weight = 1)

if __name__=="__main__":
    app = GUI()
    app.mainloop()