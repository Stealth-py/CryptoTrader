import os, sys, inspect, webbrowser
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from tkinter import *
from config import Binance
from binanceapi.binance_script import Work

help_url = "https://github.com/Stealth-py/CryptoTrader"
obj = Binance()

class BinanceAPI(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Binance API")

        self.apichoice = IntVar()
        self.api_key = StringVar()
        self.secret_key = StringVar()
        self.optionchoice = IntVar()
        self.dropchoice = StringVar()
        
        self.widgets()
        self.api_input_page()

    def widgets(self):
        """
            Creates a 'Menu()' object named 'mainmenu'
            Adds the command 'Help' which, onclick, redirects us to the github repository of this project.
            Repository: 'https://github.com/Stealth-py/CryptoTrader'
        """

        mainmenu = Menu(self)
        mainmenu.add_command(label = "Help", underline=1, command = lambda: webbrowser.open(help_url))
        self.config(menu = mainmenu)

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
        l = Label(optsmenu, image = PhotoImage("binwp.png"))
        l.place(x=0, y=0)

        min_, max_ = IntVar(), IntVar()
        min_.set(1)
        max_.set(3)

        var = IntVar()
        var.set(-1)
        var1 = StringVar()
        var1.set("Choose")

        OPTIONS = obj.SYMBOLS

        def check_radio():
            self.optionchoice = var.get()
            print(self.optionchoice)

        def check_drop():
            self.dropchoice = (var1.get())
            print(self.dropchoice)
            if self.dropchoice not in OPTIONS or not(max_.get()>=self.optionchoice>=min_.get()):
                self.options_menu()
            else:
                if self.optionchoice==1:
                    self.enquire_crypt(self.dropchoice)
                elif self.optionchoice==2:
                    self.balance()
                else:
                    print("TODO: PLOTTING THE DETAILS")


        l = Label(optsmenu, text = "Choose a symbol you want to perform the following functions for:", relief = "groove", font = ("helvetica", 12, "bold"))
        l.grid(row = 0, sticky = W)

        w = OptionMenu(optsmenu, var1, *OPTIONS)
        w.grid(row = 1, pady = 5)

        l1 = Label(optsmenu, text = "Choose any of the following options for your selected symbol:", relief = "groove", font = ("helvetica", 12, "bold"))
        l1.grid(row = 2, sticky = W)

        o1 = Radiobutton(optsmenu, text = "Enquire about the most recent details of a specific cryptocurrency", variable=var, value = 1, command = check_radio, anchor="w")
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
    
    def enquire_crypt(self, symbol):
        cryptoenquiryframe = Frame(self)
        w = Work(self.api_key, self.secret_key)
        data = w.crypto_details(symbol)
        scrollb = Scrollbar(cryptoenquiryframe)
        l = Label(cryptoenquiryframe, text = f"Details for {symbol}", fg = "red", font = ("helvetica", 15, "bold"))
        l.grid(row = 0, sticky=W)

        txt = Text(cryptoenquiryframe)
        for key in data:
            txt.insert(END, f"{key} = {data[key]} \n")
        
        txt.configure(state = DISABLED, font = ("helvetica", 11), height=25, fg = "blue", relief="sunken")
        txt.grid(row = 1)
        scrollb.config(command = txt.yview)
        scrollb.grid(row = 1, column = 5)
        
        cryptoenquiryframe.grid(row = 0, column = 0, sticky = "NESW")
        cryptoenquiryframe.grid_rowconfigure(0, weight = 1)
        cryptoenquiryframe.grid_columnconfigure(0, weight = 1)

    def balance(self):
        balanceframe = Frame(self)
        w = Work(self.api_key, self.secret_key)
        balance = w.account_balance()
        
        scrollb = Scrollbar(balanceframe)
        header = Label(balanceframe, text = "Your Account Balance", relief = "ridge", font = ("helvetica", 14, "bold"), fg = "red")
        header.grid(row = 0, sticky = W)

        txtb = Text(balanceframe)
        for key in balance:
            txtb.insert(END, f"{key} = {balance[key]} \n")
        
        txtb.configure(state = DISABLED, font = ("helvetica", 11), height = 25, fg = "blue", relief = "sunken")
        txtb.grid(row = 1)
        scrollb.config(command=txtb.yview)
        scrollb.grid(row = 1, column = 5)
        
        balanceframe.grid(row = 0, column = 0, sticky = "NESW")
        balanceframe.grid_rowconfigure(0, weight = 1)
        balanceframe.grid_columnconfigure(0, weight = 1)
    
    # def plotting(self):
        

# if __name__ == "__main__":
#     b = BinanceAPI()
#     b.enquire_crypt("ETHBTC")