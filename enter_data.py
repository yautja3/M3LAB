

from movie import Movie
from rental import Rental
from customer import Customer
# Import date time module

def enterData():
    lyst2 = []
    continue_on = 'y'
    while continue_on == 'y':
        
        custName = input("Enter the name of the customer: ")
        custName = custName.capitalize()
        custName = Customer(custName)
        lyst2.append(custName)
        
        rentTime = int(input("Enter the number of days rented: "))
        movieName = input ("Enter the name of the movie: ")
        movieName = movieName.capitalize()
        rentalData1 = Rental(movieName,"")
        lyst2.append(rentalData1)
        rentalData2 = Rental("",rentTime)
        lyst2.append(rentalData2)
        
        movieMenu = int(input("Enter the movie type: \n"
                          "Enter 1 for Children's movie.\n"
                          "Enter 2 for Regular movie.\n"
                          "Enter 3 for New Release movie.\n"))
        if movieMenu == 1:
            children = "Children's"
            regular = ''
            new_release = ''
            movieType = Movie(children,regular,new_release)
            lyst2.append(movieType)
            
        if movieMenu == 2:
            children = ""
            regular = 'Regular'
            new_release = ''
            movieType = Movie(children,regular,new_release)
            lyst2.append(movieType)
        
        if movieMenu == 3:
            children = ""
            regular = ''
            new_release = 'New-Release'
            movieType = Movie(children,regular,new_release)
            lyst2.append(movieType)
        continue_on = input("Would you like to enter more data? y or n ")
        if continue_on == 'y':
            continue
        else:
            break
    print()
    for i in lyst2:
        print(i)
        
    return lyst2