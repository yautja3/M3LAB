"""
Author: Reagan/Simchuck
Prints out a list of students
"""

import Movie
import Customer

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
    film = Movie(title, price, genre)

    #Puts the film object into the movies list
    movies.append(film)

    #Tells user what is happening
    print("The movie has been entered into the database")

    """ Note:  This is not entering the movie into a file.  I
    would like help in doing so, so if one of you guys would work on that,
    that'd be great. """




"""  The user can input new customers into the database """
def custData(customers):
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

    #Puts the film object into the movies list
    customers.append(customer)

    #Tells user what is happening
    print("The customer has been entered into the database")

    """ Note:  This is not entering the movie into a file.  I
    would like help in doing so, so if one of you guys would work on that,
    that'd be great. """

    



if __name__ == "__main__":
    main()
