#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Here's what I've done thus far.  There are two blocks of code that write to 
.csv files for movie and customer.  It's important to note that if you exit 
the program and reopen it, the data will be written over.  I can't find a way 
to append to a .csv file.  I'll continue to try and find a way to do so.  
There's still much work to be done on this and I'm going to keep working on it 
until Sunday eve.  Feel free to add to this if you have the time. 
I'll post on github what I've got then.  Please see the comments under the .csv
blocks.  Any questions/comments: psimchuk@gmail.com or 9106585268
"""

"""
Author: Reagan/Simchuk
Prints out a list of students
"""
import csv
import movie
import customer
from customer import Customer
import rental

def main():
    #Variable for recieving user answer
    answer = 0

    #Variable for containing the list of movies
    movies = []

    #Variable for containing the list of customers
    customers = []

    #A while statement that makes main run until exit is chosen
    while(answer != 6):
        print("1. Enter a movie into the film database.")
        print("2. Enter a customer into the customer database.")
        print("3. Search for a movie by title.")
        print("4. Browse a genre.")
        print("5. Save additions to file.")
        print("6. Exit")
        answer = int(input("Please make a selection  "))

        #lists the choices for the user
        if(answer==1):
            filmData(movies)
            pass
        elif(answer==2):
            custData(customers)
            pass
        elif(answer==3):
            pass
        elif(answer==4):
            pass
        elif(answer==5):
            pass
        elif(answer==6):
            exit
        else:
            print("Please choose a valid answer")


""" Allows the user to enter a film into the database """
def filmData(movies):
    #variables to enter into the Movie class
    title = ""
    price = 0.0
    genre = ""
    ans = 0

    #Take variable input from the user
    title = input("Enter the title of the movie:  ")
    price = float(input("Enter the rental cost of the movie:  "))
    ans = int(input("Is this a 1. new release, 2. children's film, or 3. other? "))

    #turn input into genre
    if(ans == 1):
        genre = "New Release"
    elif(ans == 2):
        genre = "Children's"
    elif(ans == 3):
        genre = "General"
        
    #Running the variables through the Movie class to create a film object
    film = movie.Movie(title, price, genre)

    #Puts the film object into the movies list
    movies.append(film)

    #Tells user what is happening
    print("The movie has been entered into the database")

    
    with open("movieD_base.csv",'r') as csv_file: 
        csv_reader = csv.reader(csv_file)
        with open("movieD_base.csv", 'w') as new_file:
            wr = csv.writer(new_file, delimiter=',')
            fieldnames = ['TITLE','PRICE','GENRE']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
            csv_writer.writeheader()
            for line in csv_reader:
                csv_writer.writerow(line)
            for film in movies:
                wr.writerow(film.convertToMovieList())


def custData(customers):
    """  The user can input new customers into the database """
    #variables to enter into the Customer class
    firstName = ""
    lastName = ""
    custID = 0
    rentals = [] 
    film = ""
    fees = 0.0
    ans = ''

    #Take variable input from the user
    firstName = input("Enter the first name of the customer:  ")
    lastName = input("Enter the last name of the customer:  ")
    custID = int(input("Enter a five digit ID number:  "))
    film = input("What film is the customer renting?  ")

    #film is appended directly to rentals, because customers can rent
    # more than one film and rentals is a list
    rentals.append(film)
    
    #Fees are not inputted because a new customer hasn't rented before
    # and therefore has no fees. Default 0.0 sent to the object
    customer = Customer(firstName, lastName, custID, rentals, fees)
   
    #Puts the customer object into the customer list
    customers.append(customer)
#    for j in rentals:
#        print("film rentals:",j)
    for i in customers:
        print('customers: ',i)
    #Tells user what is happening
    print("The customer has been entered into the database")


    with open("file_name.csv",'r') as csv_file: 
        csv_reader = csv.reader(csv_file)
        with open("file_name.csv", 'w') as new_file:
            wr = csv.writer(new_file, delimiter=',')
            fieldnames = ['firstName','lastName','custID','rentals','fees']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
            csv_writer.writeheader()
            for line in csv_reader:
                csv_writer.writerow(line)
            for customer in customers:
                wr.writerow(customer.convertToList())
    '''
    Note Above csv File:  If we read the existing csv file and then write both 
    the lines in the existing .csv file and any new input without creating a 
    list from the existing csv, this works only as long as we don't exit the 
    program.
    If we choose to exit the program, I believe we must create a list to hold 
    existing data and new data and then write that to the .csv file.  I don't 
    think its possible to append a .csv file without doing this, however this 
    code might work to append a .csv file:
        
    with open('document.csv','a') as fd:
        fd.write(myCsvRow)
    
    When I try to use the code above to append to a .csv file, I get an error 
    message:      TypeError: write() argument must be str, not list
    '''


if __name__ == "__main__":
    main()