# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:19:41 2022

@author: trrho
"""

import PySimpleGUI as gui
import os
import pandas as pd
runfile('GetCBPriceData_v4.py', wdir=os.environ['SETPATH'])


# Check to see if Toolkit path is in sys.path. If so, do nothing. If not, add it.
Toolpath = r'C:\Users\trrho\OneDrive\Documents\Python\Toolkit'
def pathcheck(Toolpath):
    """ (str) -> None
    
        This function inputs the 'Toolkit' path, compares it to all paths in sys.path,
        then determines if 'Toolkit' path exists in sys.path. If it does, no action is taken.
        If not, then the 'Toolkit' path is added. 
    
    """
    import sys
    counter = 0

    for i in range(len(sys.path)):
        if Toolpath == sys.path[i]:
            counter += 1
    if counter == 0:
        sys.path.insert(0, r'C:\Users\trrho\OneDrive\Documents\Python\Toolkit')

# Run function above to check for 'Toolkit' path in sys.path
pathcheck(Toolpath)

from Toolkit import money, percentage

# sets color theme of window. To preview all themes, use psg.theme_previewer()
gui.theme('Darkblue3')

size = (15,1)

layout = [[gui.Text('Swan Bitcoin Dashboard!!!')],
           [gui.FileBrowse(button_text = 'Select File',initial_folder = r'C:\Users\trrho\OneDrive\Documents\Finance\Investments\Crypto\Bitcoin\Swan',
                           target = 'File',size = size, enable_events=True),
           gui.Input(key = 'File')],
           [gui.Text('Total BTC Saved',size = size),  gui.InputText(key = 'TotalBTCSaved')],
           [gui.Text('BTC Price',size = size),  gui.InputText(key = 'Price')],
           [gui.Text('Current Value',size = size),  gui.InputText(key = 'CV')],
           [gui.Text('% Change',size = size), gui.InputText(key = 'Perc')],
           [gui.Button(button_text = 'Load File'), gui.Cancel()]
    
          
          
         ]



# Create the Window
window = gui.Window('Futtbuckers', layout)
# Event Loop to process "events" and get the "values" of the inputs

# It appears that the FileBrowse (Select File) button does not execute the code below. If clicking 
# it then exiting (with X), all values have NoneType. However, using any other button, even if the
# button does nothing, this loop is executed and values are now populated with the GUI info. 
while True:
    event, values = window.read()
#    gui.popup(event,values)
    if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    # When 'Load File' button is pressed, do a bunch of things:
    # 1. Read excel file
    # 2. Get current bitcoin price from GetCBPriceData_v4
    # 3. import Toolkit (use sys or os???) os requires changing directory
    if event == 'Load File':
#        event, values = window.read()
        print('you clicked the button!')
        # Split file path and name into separate strings for ease of use. Not really necessary...
        
        [Path, Name] = os.path.split(values['File'])
        
        # Determine if file is an excel file. stop if not '.xls***'
        ext = os.path.splitext(Name)
        
        try:
            ext[1][:4] == '.xls'
        except XLRDError:
            print('Incorrect file format. Please choose an excel file!')
       #     return#
            
            
        
    # Read excel file. Worry about error handling later
        Data = pd.read_excel(values['File'])
        
        # Column headers
        Columns = Data.columns
        # Creates dataframe with only purchases
        PurchaseData = Data[Data['Event'] == 'purchase'].reset_index(drop=True)
    
        # Creates dataframe with only deposits
        DepositData = Data[Data['Event'] == 'deposit'].reset_index(drop=True)
    
        # Sum of all deposits in USD
        TotalDeposits = DepositData['USD'].sum()
        # Sum of all BTC purchased
        TotalBTC = PurchaseData['Unit Count'].sum()
        # Sum of all BTC prices at time of purchase. Not sure what I'm doing here...
        TotalBTCPrice = PurchaseData['BTC Price'].sum()
        # Total amount of USD used to purchase BTC
        TotalUSD = PurchaseData['USD'].sum()
        # Current total value of BTC in USD
        TotalValue = float(price.amount) * TotalBTC
    
        AvgCB = TotalBTCPrice
    
        # 
        # print('Current BTC Price: ' + money(float(price.amount)))
        # print('Total BTC Accumulated: ' + str(TotalBTC))
        # print('Total USD Deposits: ' + money(TotalDeposits))
        # print('Total Invested USD Deposits: ' + money(TotalUSD))
        # print('Total Portfolio Value: ' + money(TotalValue))
    
        Perc = ((TotalValue - TotalUSD) / TotalUSD) * 100
    
        # print('Percent change: ' + percentage(Perc))
    
        # This counts all deposits and purchases and determines if there are any deposits left
        # / days left to buy
        Buffer = Data[Data['Event'] == 'deposit']['USD'].sum() - Data[Data['Event'] == 'purchase']['USD'].sum()
        # TotalBTC = Data[Data[]]
    
    # Update window with calculated values from above     
        window['TotalBTCSaved'].update(TotalBTC)
        window['Price'].update((money(float(price.amount))))
        window['CV'].update(money(TotalValue))
        window['Perc'].update(percentage(Perc))
    
    
#    print(values)   

window.close()