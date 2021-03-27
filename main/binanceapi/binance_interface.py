import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from tkinter import *
from config import Binance
from binanceapi.binance_script import Work

obj = Binance()

class BinanceAPI(Tk):
    def __init__(self):
        Tk.__init__(self)

        l = Label(self, image = PhotoImage("binwp.png"))
        l.place(x=0, y=0)

        self.apichoice = IntVar()
        self.api_key = StringVar()
        self.secret_key = StringVar()
        self.optionchoice = IntVar()
        self.dropchoice = StringVar()

        self.api_input_page()

    def api_input_page(self):
        apiframe = Frame(self)
        l = Label(apiframe, image = PhotoImage("binwp.png"))
        l.place(x = 0, y = 0, relwidth=1, relheight=1)

        e1 = StringVar()
        e2 = StringVar()

        def submit():
            self.api_key = e1.get()
            self.secret_key = e2.get()
            w = Work(self.api_key, self.secret_key)
            if w.response_check():
                self.options_menu()
            else:
                self.api_input_page()

        l1 = Label(apiframe, height = 1, relief = "groove", text = "API KEY", font = ("helvetica", 10, "bold"))
        l1.grid(row = 0, sticky = "NESW", padx = 5)
        l2 = Label(apiframe, height = 1, relief = "groove", text = "SECRET KEY", font = ("helvetica", 10, "bold"))
        l2.grid(row = 1, sticky = "NESW", padx = 5)

        e1 = Entry(apiframe, textvariable = self.api_key, bd = 2)
        e1.grid(row = 0, column = 2, padx = 5)
        e2 = Entry(apiframe, textvariable = self.secret_key, bd = 2, show = "*")
        e2.grid(row = 1, column = 2, padx = 5)

        b = Button(apiframe, text = "Submit", command = lambda: [submit(), apiframe.destroy(), self.geometry("700x500")])
        b.grid(row = 2, column = 1)

        apiframe.grid(row = 0, column = 0, sticky = "NESW")
        apiframe.grid_rowconfigure(0, weight=1)
        apiframe.grid_columnconfigure(0, weight=1)

    def options_menu(self):
        optsmenu = Frame(self)

        var = IntVar()
        var1 = StringVar()
        var1.set("Choose")

        def check_radio():
            self.optionchoice = var.get()
            print(self.optionchoice)

        def check_drop():
            self.dropchoice = (var1.get())
            print(self.dropchoice)

        OPTIONS = obj.SYMBOLS

        l = Label(optsmenu, text = "Choose a symbol you want to perform the following functions for:", relief = "groove", font = ("helvetica", 12, "bold"))
        l.grid(row = 0, sticky = W)

        w = OptionMenu(optsmenu, var1, *OPTIONS)
        w.grid(row = 1, pady = 5)

        l1 = Label(optsmenu, text = "Choose any of the following options for your selected symbol:", relief = "groove", font = ("helvetica", 12, "bold"))
        l1.grid(row = 2, sticky = W)

        o1 = Radiobutton(optsmenu, text = "Enquire about a specific cryptocurrency", variable=var, value = 1, command = check_radio, anchor="w")
        o1.grid(row = 3, sticky = W)
        o2 = Radiobutton(optsmenu, text = "Enquire about your account balance", variable = var, value = 2, command = check_radio, anchor = "w")
        o2.grid(row = 4, sticky = W)
        o3 = Radiobutton(optsmenu, text = "Plot a graph and analyse the historical data of the chosen symbol", variable = var, value = 3, command = check_radio, anchor = "w")
        o3.grid(row = 5, sticky = W)

        b = Button(optsmenu, text = "Next", command = lambda: [check_drop(), optsmenu.destroy()], anchor = "center")
        b.grid(row = 7)

        optsmenu.grid(row = 0, column = 0, sticky = "NESW")
        optsmenu.grid_rowconfigure(0, weight=1)
        optsmenu.grid_columnconfigure(0, weight=1)