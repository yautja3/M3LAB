#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:25:42 2018

@author: petersimchuk/bethanyreagan
"""


class Customer (object):
    def __init__(self, firstName, lastName, custID, rentals, fees):
        self.firstName = firstName
        self.lastName = lastName
        self.custID = custID
        self.rentals = rentals
        self.fees = fees
    def __str__(self):
        text = self.firstName + self.lastName + str(self.custID) +
        str(rentals) + str(fees)
        return text
        
#        return str(self.customer)
#        return str("Customer Name:  " + self.customer)


#Later we should come up with a way to calculate fees and update the list
# with them
