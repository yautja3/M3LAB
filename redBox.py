

from movie import Movie
from rental import Rental
from customer import Customer
# Import date time module

# Create while loop
lyst2 = []

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
print()
for i in lyst2:
    print(i)

# Create module named: writeTextFile.py
col_format = "{:<15}"*4+'\n'
col_format2 = "{:<15}"*1
open_file = open("RedBox.txt",'a')

open_file.write(col_format.format("Customer Name","Movie Title","Days Rented","Type Movie"))
for i in lyst2:
    i = str(i)
    open_file.write(col_format2.format(i))




open_file.close()   







