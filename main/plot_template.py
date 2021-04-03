import datetime
from tkinter import font
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd

def candlestick_plot(data):
    data_clean = {"Date": [], "Open": [], "High": [], "Low": [], "Close": []}
    for i in data:
        data_clean["Date"].append(datetime.datetime.fromtimestamp(i[0]/1000))
        data_clean["Open"].append(float(i[1]))
        data_clean["High"].append(float(i[2]))
        data_clean["Low"].append(float(i[3]))
        data_clean["Close"].append(float(i[4]))

    data_clean = pd.DataFrame(data_clean)

    data_clean["Date"] = pd.to_datetime(data_clean["Date"])
    data_clean["Date"] = data_clean["Date"].apply(mpl_dates.date2num)

    fig, ax = plt.subplots()

    candlestick_ohlc(ax, data_clean.values, width = 0.2, colorup = "blue", colordown="red", alpha=0.8)

    ax.grid()

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    fig.suptitle("Candlestick chart for OHCLV of the given symbol")

    ax.xaxis.set_major_formatter(mpl_dates.DateFormatter("%d-%m-%y"))

    fig.autofmt_xdate()
    fig.tight_layout()

    return fig