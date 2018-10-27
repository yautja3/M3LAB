"""
Author: Reagan
Prints out a list of students
"""

"""
WARNING: This program does not write to file.  Any changes made will not
be saved.
"""

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
        print("5. Rent a movie to a customer.")
        print("6. Take payment from customer.")
        print("7. Exit")
        answer = int(input("Please make a selection  "))

        #lists the choices for the user
        if(answer==1):
            loadCust(filename1, customers)
        elif(answer==2):
            loadMovie(filename2, movies)
        elif(answer==3):
            showRenters(customers)
        elif(answer==4):
            pass
        elif(answer==5):
            pass
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
            cust = [Customer(firstName, lastName, custID, renting)]
            customers.append(cust)

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
            film = Movie(title, ID, genre, out, rentedBy, daysOut, daysOver)
            movies.append(film)

    print("\nMovie file has been loaded\n")


def showRenters(customers):
    #check and see if the customers list is loaded
    if(len(customers) == 0):
        print("\nCustomer file has not been loaded!\n")

    #print all customers who have stuff rented out
    for customer in customers:
        if(customer[3]=="yes"):
            print(customer[0],customer[1])



""" Shows any customers who haven't turned in movies during rental period """
def showOverdue(customers, movies):
    #search movies for daysOver > 0
    #print customers that match customer code in movie file.



""" Helps customer rent a movie """
def rentFilm(customers, movies):
    #Enter a customer's name and search if in database already

    #If not in database, enter customer information
    #   customer ID is their firstName lastName initials, and some random #s

    #If in database, ask for name of movie
    #   if movie not in database, reject.
    #   if movie in database, match customer id in to movie object, reset
    #       days out to 0, days overdue to 0



""" helps customer pay bill """
def payBill(customers, movies):
    #search for customer
    #list customer fees

    #make a payment
    #reset fees as fees - payment, except not lower than zero.

    

    

""" Customer class to create customer objects """
class Customer:
    def __init__(self, firstName, lastName, custID, renting):
        self.firstName = firstName
        self.lastName = lastName
        self.custID = custID
        self.renting = renting


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
        
    



if __name__ == "__main__":
    main()