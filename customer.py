#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:25:59 2018

@author: petersimchuk
"""

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
        text = self.firstName +' ' + self.lastName +'\n' + str(self.custID) + '\n' + str(self.rentals) + '\n' + str(self.fees)
        return text
    
    def convertToList(self):
        '''This is a method that returns the contents of a class to a list to populate a csv file'''
        custLyst = [self.firstName,self.lastName,str(self.custID),str(self.rentals),str(self.fees)]

        return custLyst
#        return str(self.customer)
#        return str("Customer Name:  " + self.customer)


#Later we should come up with a way to calculate fees and update the list
# with them