#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:21:15 2018

@author: petersimchuk
"""

class Movie(object):
    def __init__(self, children, regular, new_release):
        self.children = children
        self.regular = regular
        self.new_release = new_release
    def __str__(self):
        return str(self.children) + str(self.regular) + str(self.new_release)
#        return "Type Movie:  " + str(self.children) + str(self.regular) + str(self.new_release)


#    def set_children(self, children):
#        self.children = children
#    def set_regular(self,regular):
#        self.regular = regular
#    def set_new_release(self,new_release):
#        self.new_release = new_release
#        
#    
#    def get_children(self,children):
#        return self.children
#    def get_regular(self,regular):
#        return self.regular
#    def get_new_release(self,new_release):
#        return self.new_release
