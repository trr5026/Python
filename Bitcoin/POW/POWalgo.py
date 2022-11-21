# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:57:16 2022

Bitcoin Proof of Work Algorithm in Python!

@author: trrho
"""


# MAX_TARGET
# in hex, always represented as '1D00FFFF' where 1D = exponential (e), 00FFFF = coefficient (c)
# of the following equation: MAX_TARGET = c * 2 ** (8*(e-3))
# first, convert e and c to decimal, solve the above equation, then convert back to hex
# only to convert back to decimal to divide by the current target to get the difficulty. 
# super simple and obvious, right?!?!

# current target is determined using the same equation above, coming from the 'bits'
# field of a given block. This field only changes when the difficulty changes every 2016 blocks

MThex = '1D00FFFF'
E = '1D'
C = '00FFFF'
e = int(E,16)
c = int(C,16)
mt = c * 2 ** (8*(e-3))

# apply same formula to target


import hashlib
import time

max_nonce = 2 ** 32 # 4 billion

def proof_of_work(header, difficulty_bits):
    # calculate the difficulty target
    target = 2 ** (256-difficulty_bits)
    
    for nonce in range(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()
        # check if this is a valid result, below the target
        if long(hash_result, 16) < target:
            print( "Success with nonce %d" % nonce)
            print( "Hash is %s" % hash_result)
            return (hash_result,nonce)
        print( "Failed after %d (max_nonce) tries" % nonce)
        return nonce
    
    if __name__ == '__main__':
        nonce = 0
        hash_result = ''
        # difficulty from 0 to 31 bits
        for difficulty_bits in range(32):
            difficulty = 2 ** difficulty_bits
            print( "Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
            print( "Starting search...")
            
            # checkpoint the current time
            start_time = time.time()
            
            # make a new block which includes the hash from the previous block
            # we fake a block of transactions - just a string
            new_block = 'test block with transactions' + hash_result

            # find a valid nonce for the new block
            (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)
            # checkpoint how long it took to find a result
            end_time = time.time()
            elapsed_time = end_time - start_time
            print( "Elapsed Time: %.4f seconds" % elapsed_time)
            
            if elapsed_time > 0:
                # estimate the hashes per second
                hash_power = float(long(nonce)/elapsed_time)
                print( "Hashing Power: %ld hashes per second" % hash_power)