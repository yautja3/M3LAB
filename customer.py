#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:25:42 2018

@author: petersimchuk
"""


class Customer (object):
    def __init__(self, customer):
        self.customer = customer
    def __str__(self):
        return str(self.customer)
#        return str("Customer Name:  " + self.customer)