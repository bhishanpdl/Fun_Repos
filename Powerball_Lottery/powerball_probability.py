#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Date        : Jun 13, 2017 Tue
# Last update : 
#
# Required answer: 292,201,338
# Imports
from scipy.misc import comb
import sympy
import math


# How to calculate combinations in python?
def calculate_probability():
    prob1 = comb(69,5) 
    prob2 = sympy.binomial(26,1)
    prob = prob1 * prob2
    
    print('prob =  {0:,}'.format(int(prob)))
    return int(prob)
    
def years_to_win_lottery():
    prob = calculate_probability()
    century, day = divmod(prob,36500)
    year,days = divmod(prob,365)
    
    print('If you buy a ticket everyday and you are immortal, you may win\
    \b\b\b\b the jackpot after %d centuries and %d days!'%(century,day))
    
    print('\nIf you want to count in years, you will win lottery \
    in %d years and %d days.'%(year,days))


    
if __name__ == '__main__':
    prob = calculate_probability()
    years_to_win_lottery()


# From wikipedia:
# Drawings are held Wednesday and Saturday evenings at 10:59 p.m. Eastern Time. 
# Since October 7, 2015, the game has used a 5/69 (white balls) + 1/26 
# (Powerballs) matrix from which winning numbers are chosen, resulting 
# in odds of 1 in 292,201,338 of winning a jackpot per play.

# 1 yr = 365 days
# 1 century = 100 * 365 = 36500 days
# 1 millinium = 1000 * 365 = 365000
