# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 17:50:57 2022

v2: bitcoin column header changed in CSV file from 'BTC' to 'Unit Count'
Updated GetCBPriceData_v3 to v4: no longer prints BTC price, instead returns price variable

v3: moved to new folder location to hopefully improve organization 

@author: trrho
"""
import os
# Gets current BTC price. Stores value in variable price.amount
runfile('GetCBPriceData_v4.py',wdir=os.environ['SETPATH'])


# append tools directory to sys.path to use money function (convert number to USD format)
# as well as percentage str output
#import sys

# Check to see if Toolkit path is in sys.path. If so, do nothing. If not, add it.
Toolpath = r'C:\Users\trrho\OneDrive\Documents\Python\Toolkit'

def pathcheck(Toolpath):
    """ (str) -> None
    
        This function inputs the 'Toolkit' path, compares it to all paths in sys.path,
        then determines if 'Toolkit' path exists in sys.path. If it does, no action is taken.
        If not, then the 'Toolkit' path is added. 
    
    """
    import sys
    counter =  0
    
    for i in range(len(sys.path)):
        if Toolpath == sys.path[i]:
            counter += 1
    if counter == 0:
        sys.path.insert(0, r'C:\Users\trrho\OneDrive\Documents\Python\Toolkit')

# Run function above to check for 'Toolkit' path in sys.path
pathcheck(Toolpath)

from Toolkit import money, percentage


os.chdir(r'C:\Users\trrho\OneDrive\Documents\Finance\Investments\Crypto\Bitcoin\Swan')

import pandas as pd



# Read excel sheet data as csv and store as dataframe
Data = pd.read_excel('Swan_Deposits.xlsx')

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
print('Current BTC Price: ' + money(float(price.amount)))
print('Total BTC Accumulated: ' + str(TotalBTC))
print('Total USD Deposits: ' + money(TotalDeposits))
print('Total Invested USD Deposits: ' + money(TotalUSD))
print('Total Portfolio Value: ' + money(TotalValue))

Perc = ((TotalValue - TotalUSD) / TotalUSD) * 100

print('Percent change: ' + percentage(Perc))


# This counts all deposits and purchases and determines if there are any deposits left
# / days left to buy
Buffer = Data[Data['Event'] == 'deposit']['USD'].sum() - Data[Data['Event'] == 'purchase']['USD'].sum()
#TotalBTC = Data[Data[]]

