import requests
from tkinter import *
import tkinter

url = "https://api.coinmarketcap.com/v1/ticker/?limit=400"

CoinList = requests.get(url)

SwitchStatus = False


def calc():
    global status
    global CoineOne
    global CoinAmount
    global SwitchStatus
    
    counter = 0
    #Set up pre Failure case assuming that Alt Coin isn't found
    CoinOnePrice = False
    #Loop through Json to find the Alt coin while also trying to find ETH and grab the price of it
    while counter < len(CoinList.json()):
        if CoinList.json()[counter]["symbol"].upper() == str(CoinOne.get()).upper():
            CoinOnePrice = CoinList.json()[counter]["price_usd"]
        if CoinList.json()[counter]["symbol"].upper() == "ETH":
            ETHPrice = CoinList.json()[counter]["price_usd"]
        counter += 1
    #Coin not found
    if CoinOnePrice == False:
        status.configure(text="Coin Not Found")
    else:
        #If SwitchStatus == False then the program Converts Alt Coin to ETH, If SwitchStatus == True then the program converts the amount entered of ETH into Alt coins
        if SwitchStatus == False:
            CoinOneAmountUSD = float(CoinOnePrice) * float(CoinAmount.get())
            ETHAmount = float(CoinOneAmountUSD) / float(ETHPrice)
            EndUSD = float(ETHPrice) * float(ETHAmount)
            status.configure(text=str(ETHAmount) + " ETH or " + str(EndUSD) + " USD")
        else:
            CoinOneAmountUSD = float(ETHPrice) * float(CoinAmount.get())
            ETHAmount = float(CoinOneAmountUSD) / float(CoinOnePrice)
            EndUSD = float(CoinOnePrice) * float(ETHAmount)
            status.configure(text=str(ETHAmount) + " " + str(CoinOne.get()).upper() + " or " + str(EndUSD) + " USD")
        
        
        
#Button to switch from converting alt coin to ETH or ETH to alt coin        
def switch():
    global SwitchStatus
    global status
    
    if SwitchStatus == False:
        SwitchStatus = True
        status.configure(text="Converting ETH to Desired Coin")
    else:
        SwitchStatus = False
        status.configure(text="Converting Desired Coin to ETH")

        
        
        
    #GUI Creation    
window = tkinter.Tk()
window.title("Desired Coin to ETH")
    


ConvertButton = Button(window, text= "Convert", command=calc, bg='green', fg='black')
ConvertButton.grid(row=2,column=1, sticky=E+W)
SwitchButton = Button(window, text = "Switch Coins", command = switch, bg='red', fg='black').grid(row=2,column=0, sticky=E+W)
CoinOne = Entry(window)
CoinOne.grid(row=0, column=1, sticky=E)
LabelCoin = Label(window, text = "Desired Coin:").grid(row=0, column=0, sticky=W)
LabelAmount = Label(window, text = "Coin Amount:").grid(row=1, column=0, sticky=W)
CoinAmount = Entry(window)
CoinAmount.grid(row=1, column=1, sticky=E)
status = Label(window, width = 40, text = "Converting Desired Coin to ETH")
status.grid(row=3, columnspan=2)




window.resizable(width=False, height=False)
window.mainloop()

