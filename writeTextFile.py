#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:02:16 2018

@author: petersimchuk
"""
import enter_data

def createTextFile(lyst2): 
    
    col_format = "{:<15}"*4+'\n'
    col_format2 = "{:<15}"*1
    text_file = open("RedBox.txt",'a')
    
    text_file.write(col_format.format("Customer Name","Movie Title","Days Rented","Type Movie"))
    for i in lyst2:
        i = str(i)
        text_file.write(col_format2.format(i))
        
    text_file.close() 