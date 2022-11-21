# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:23:34 2022

This function inputs the bitcoin 4-byte difficulty target as a string and outputs
the network difficulty as a float

Difficulty Calculator
# MAX_TARGET
# in hex, always represented as '1D00FFFF' where 1D = exponential (e), 00FFFF = 
coefficient (c)  of the following equation: MAX_TARGET = c * 2 ** (8*(e-3))
# first, convert e and c to decimal, solve the above equation, then convert back
# to hex only to convert back to decimal to divide by the current target to get
 the difficulty. super simple and obvious, right?!?!

# current target is determined using the same equation above, coming from the 
'bits' field of a given block. This field only changes when the difficulty 
changes every 2016 blocks

MThex = '1D00FFFF'
E = '1D'
C = '00FFFF'
e = int(E,16)
c = int(C,16)
mt = c * 2 ** (8*(e-3))

# apply same formula to target

@author: trrho
"""

MThex = '1D00FFFF'
E = '1D'
C = '00FFFF'
e = int(E,16)
c = int(C,16)
mt = c * 2 ** (8*(e-3))

def DifficultyCalculator(bits):
    
        
    Et = bits[0:2]
    Ct = bits[3:]
    
    et = int(Et,16)
    ct = int(Ct,16)
    curtarget = ct * 2 ** (8*(et-3))
    
    Difficulty = mt / curtarget
    
    return Difficulty
    
