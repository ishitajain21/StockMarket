import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

''' Takes a stock ticker symbol,
start month, 
start year,
and period of time

returns 
amount invested,amount earned if the stock was bought on a certain day and sold on a certain day. 

Tells customer which date to buy and sell to maximise return

 '''


try:
    dict_stockprice = {}
    # dict with {stockprice: date}

    def calc_max_price_day():
        return dict_stockprice[max(d_keys)]


    tick = input("What is the Ticker symbol? ")
    tick = tick.lower()

    start_month = input("Write the start month. In number form. (06) ")
    start_year = input("Write the start year. In number form. (2020) ")
    year = int(input("How many years since?"))
    month = int(input("How many months since?"))


    how_many = int(input("How much money do you want to put in?"))
    start_date =  start_year + "-" + start_month + "-01" 

    tick_data = yf.Ticker(tick)
    # 1st step in basic data

    start_date_to_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_to_datetime = start_date_to_datetime + relativedelta(years=+year,months=+month)
    end_date = end_date_to_datetime.strftime("%Y-%m-01")


    tick_history = tick_data.history(start=start_date,end=end_date,interval="1wk")
    print(tick_history)
    # filtering with the dates.
    dict_of_history = dict(tick_history["High"])
    # filtering by having the highs only in the list as a dict

    for i in dict_of_history:
        k = i.to_pydatetime()
        # converts type(timestamp) to datetime
        try:
            dict_stockprice[dict_of_history[i]] = k
        except:
            pass
        # switches key value pair from {date:stockprice} to {stockprice:date}


    d_keys = list(dict_stockprice.keys())
    min_price_day = dict_stockprice[min(d_keys)]
    # finds the minimum price of the stock
    max_price_day = calc_max_price_day()
    #finds the max price of the stock

    while min_price_day >= max_price_day:
        # if the date of the max is less than the date of the min
        print("HIII(IIiiIiIIiiiIIIiIiiIIIIIII")
        try:
            d_keys.remove(max(d_keys))
            max_price_day = calc_max_price_day()
        except:
            d_keys = list(dict_stockprice.keys())
            max_price_day = calc_max_price_day()
            min_price_day = dict_stockprice[min(d_keys)]
            while min_price_day >= max_price_day:
                print("Min_Price")
                d_keys.remove(min(d_keys))
                min_price_day = dict_stockprice[min(d_keys)]


    am = how_many/min(d_keys)
    # amount of stock owned
    print("The amount you invested is $", round(am*min(d_keys),2))
    print("The amount you earned is $", round(am*max(d_keys),2))
    print("You should have bought", tick.upper(), "at",min_price_day,".\nYou should have sold it at",max_price_day, ".Regrets!")
    print("You earn about $",round(am*(max(d_keys)-min(d_keys)),2))

except:
    print("Something went wrong. Please use another sticker.")
