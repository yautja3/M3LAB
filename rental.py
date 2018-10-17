#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:25:05 2018

@author: petersimchuk
"""


class Rental(object):
    def __init__(self, movie, daysRented):
        self.movie = movie
        self.daysRented = daysRented
    def __str__(self):
        return str(self.movie)+ str(self.daysRented)
#        return "Movie Name:  " + str(self.movie)+ '\nDays Rented:  '+str(self.daysRented)
    
