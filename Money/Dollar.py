# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 18:04:09 2022

This function converts a float to $ format and returns dollas holla

@author: trrho
"""

def money(float):
    """ (float) -> str
    This function inputs a float value and returns a string in the form of dolla
    dolla bill yall!
    
    """
    dollas = '${:,.2f}'.format(float)
    return dollas