#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:46:00 2018

@author: petersimchuk
"""
'''
Bethany.  I tried to do an invoice method.  Please see comment at the method above classes.  Help!
'''
import csv

def main():
    #Variable for recieving user answer
    answer = 0

    #Variable for containing the list of movies
    movies = []

    #Variable for containing the list of customers
    customers = []

    #Here are our filenames
    filename1 = 'customerdatabase.csv'
    filename2 = 'moviedatabase.csv'

    #A while statement that makes main run until exit is chosen
    while(answer != 7):
        print("1. Load customers database.")
        print("2. Load movies database.")
        print("3. Display currently renting customers.")
        print("4. Display overdue customers.")
        print("5. Display the invoice.")
#        print("5. Rent a movie to a customer.")
        print("6. Take payment from customer.")
        print("7. Exit")
        answer = int(input("Please make a selection  "))

        #lists the choices for the user
        if(answer==1):
            loadCust(filename1, customers)
        elif(answer==2):
            loadMovie(filename2, movies)
        elif(answer==3):
            showRenters(customers,movies)
        elif(answer==4):
            showOverdue(customers,movies)
        elif(answer==5):
            printInvoice(customers,movies)
        elif(answer==6):
            pass
        elif(answer==7):
            exit
        else:
            print("Please choose a valid answer")


""" This loads the customers into the program"""
def loadCust(filename, customers):
    firstName = ""
    lastName = ""
    custID = ""
    # Checks if customer is currently renting anything
    renting = ""

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            firstName = row[0]
            lastName = row[1]
            custID = row[2]
            renting = row[3]
            customer = Customer(firstName, lastName, custID, renting)
            customers.append(customer)
            print(customer.lastName, customer.firstName)

    print("\nCustomer file has been loaded\n")
    


def loadMovie(filename, movies):
    title = ""
    ID = ""
    genre = ""
    # Checks to see if a movie is in or out.
    out = ""
    rentedBy = ""
    # Days a movie has been rented out
    daysOut = 0
    # Days a movie is over the rental limit
    daysOver = 0

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            title = row[0]
            ID = row[1]
            genre = row[2]
            out = row[3]
            rentedBy = row[4]
            daysOut = row[5]
            daysOver = row[6]
#            daysOut = int(row[5])
#            daysOver = int(row[6])
            movie = Movie(title, ID, genre, out, rentedBy, daysOut, daysOver)
            movies.append(movie)
            

    print("\nMovie file has been loaded\n")

def showRenters(customers,movies):
#def showRenters(customers):
    #check and see if the customers list is loaded
    if len(customers) == 0:
#    if(len(customers) == 0):
        print("\nCustomer file has not been loaded!\n")
    if len(movies) == 0:
#    if(len(movies) == 0):
        print("\nCustomer file has not been loaded!\n")

    #print all customers who have stuff rented out
    print("\nThese are the people currently renting from us: ")
    for customer in customers:
        #print(customer)
        if(customer.renting =="yes"):
            print("\t",customer.firstName,customer.lastName,)
    print("\n")



""" Shows any customers who haven't turned in movies during rental period """
'''
Bethany:  Placed an 'else' stmnt and changed int(0) to str(0).  This way those who are not
overdue do not show up.  
'''
#def showOverdue(customers, movies):
#    print("\n", "These customers are overdue:")
#    for movie in movies:
#        if(movie.daysOver != 0):
#            for customer in customers:
#                if(movie.rentedBy == customer.custID):
#                    print(customer.firstName, customer.lastName, "is", movie.daysOver,
#                          "days overdue with movie:", movie.title)
     
def showOverdue(customers, movies):
    print("\n", "These customers are overdue:")
    for movie in movies:
        if(movie.daysOver == '0'):
            pass
        else:
            for customer in customers:
                if(movie.rentedBy == customer.custID):
                    print(customer.firstName, customer.lastName, "is", movie.daysOver,
                          "days overdue with movie:", movie.title)
    print("\n")
                
    #search movies for daysOver > 0
    #print customers that match customer code in movie file.
    pass


""" Helps customer rent a movie """
def rentFilm(customers, movies):
    #Enter a customer's name and search if in database already

    #If not in database, enter customer information
    #   customer ID is their firstName lastName initials, and some random #s

    #If in database, ask for name of movie
    #   if movie not in database, reject.
    #   if movie in database, match customer id in to movie object, reset
    #       days out to 0, days overdue to 0
    pass


""" helps customer pay bill """
def payBill(customers, movies):
    #search for customer
    #list customer fees

    #make a payment
    #reset fees as fees - payment, except not lower than zero.
    pass
'''Bethany.  Help!  It shows that Sharon Hobbit is two days overdue, but when I run this it shows that she is 
0 days overdue.  Why isn't Sharon's overdue days 'linked' with her name?  Help!
'''   
def printInvoice(customers,movies):
    custFname = input("Enter the customer's first name: ")
    custLname = input("Enter the customer's last name: ")
    for movie in movies:
        total = int(movie.daysOver) * 2
    for customer in customers:
        if custFname == customer.firstName and custLname == customer.lastName:
            
            print(customer.firstName,customer.lastName, "\nMovie:", movie.title, "\nDays Overdue:",movie.daysOver,
                          "\nTotal Price:", total )
   
    
    

""" Customer class to create customer objects """
class Customer:
    def __init__(self, firstName, lastName, custID, renting):
        self.firstName = firstName
        self.lastName = lastName
        self.custID = custID
        self.renting = renting

    def setFirst(self, firstName):
        self.firstName = firstName
    def setLast(self, lastName):
        self.lastName = lastName
    def setID(self, custID):
        self.custID = custID
    def setRenting(self, renting):
        self.renting = renting

    def getFirst(self):
        return self.firstName
    def getLast(self):
        return self.lastName
    def getID(self):
        return self.custID
    def getRenting(self):
        return renting


""" Movie class to create movie objects """
class Movie:
    def __init__(self, title, ID, genre, out, rentedBy, daysOut, daysOver):
        self.title = title
        self.ID = ID
        self.genre = genre
        self.out = out
        self.rentedBy = rentedBy
        self.daysOut = daysOut
        self.daysOver = daysOver

    def setTitle(self, title):
        self.title = title
    def setID(self, ID):
        self.ID = ID
    def setGenre(self, genre):
        self.genre = genre
    def setOut(self, out):
        self.out = out
    def setRentedBy(self, rentedBy):
        self.rentedBy = rentedBy
    def setDaysOut(self, daysOut):
        self.daysOut = daysOut
    def setDaysOver(self, daysOver):
        self.daysOver = daysOver

    def getTitle(self):
        return self.title
    def getID(self):
        return self.ID
    def getGenre(self):
        return self.genre
    def getOut(self):
        return self.out
    def getRentedBy(self):
        return self.rentedBy
    def getDaysOut(self):
        return self.daysOut
    def getDaysOver(self):
        return self.daysOver
        
    



if __name__ == "__main__":
    main()