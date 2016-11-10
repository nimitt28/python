# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:23:15 2016
@author: Nimitt Bhatt
"""

# Generator function of all Prime numbers
def genPrimes():
    # Initialize with the first prime number 2 in a list
    pn = [2]   
    yield pn[-1]
    nn = 3
    # Infinite loop over all positive integers 
    while True:
        NotPrime = False        
        # Check divisibility with all primes found so far        
        for el in pn:
            if nn % el == 0:
                NotPrime = True
                break
        if NotPrime:
            # Increment number and continue to next
            nn += 1
            continue
        #Prime found thus yield it
        pn.append(nn)
        nn += 1
        yield pn[-1]
