#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jun-17-2017 Sat
# Last update : 
#
#
# Imports
import random

def create_powerball_ticket():
    """ Generate 5 white ball from 1-69 including, and 
    one red ball from 1-26 including. """
    
    try:    
        num_tickets = input("How many tickets do you want?  ")
        num_tickets = int(num_tickets)
    except:
        print("Please Enter a valid number.")
        
        # Start over again
        num_tickets = input("How many tickets do you want?  ")
        num_tickets = int(num_tickets)
        
    
    # Print the ticket
    for nt in range(num_tickets):
        white = random.sample(range(1, 70, 1), 5) # Non-repeating 5 nums.
        red = random.randint(1,26)
        print('Ticket %d: Lottery nums =  %s and  Powerball is %d'%
        (nt+1, str(white), red))
    
    
if __name__=="__main__":
    create_powerball_ticket()
    
