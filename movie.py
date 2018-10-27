#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:24:50 2018

@author: petersimchuk
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:21:15 2018

@author: petersimchuk/bethanyreagan
"""

class Movie(object):
    def __init__(self, title, price, genre):
        self.title = title
        self.price = price
        self.genre = genre
    def __str__(self):
        return str(self.title) + str(self.price) + str(self.genre)
#        return "Type Movie:  " + str(self.children) + str(self.regular) + str(self.new_release)
    def convertToMovieList(self):
        '''This is a method that returns the contents of a movie to a list to populate a csv file'''
        movieLyst = [self.title,str(self.price),str(self.genre)]
        return movieLyst
        

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