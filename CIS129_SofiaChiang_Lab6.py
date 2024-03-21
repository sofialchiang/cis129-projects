# Sofia Chiang (Arroyo)
#CIS 129 Lab, 03/21/2024
#This program calculates the number of hot dogs and hot dog buns needed and how many will be leftover depending on how many people will be attending

import math

def main():
    #Declare variable for total number of hotdogs needed
    total = getTotalHotDogs()

    #Hot dogs in a package
    hotDogs = 10   
    #Hot dog buns in a package
    hotDogBuns = 8

    #Leftover hot dogs
    dogsLeft = 0  
    #Leftover buns
    bunsLeft = 0  

    #Calculate the number of leftover hot dogs
    dogsLeft = (hotDogs - total % hotDogs) % hotDogs

    #Calculate the minimum number of packages of hot dogs
    minDogs = math.ceil(total / hotDogs)

    #Calculate the number of leftover hot dog buns
    bunsLeft = (hotDogBuns - total % hotDogBuns) % hotDogBuns

    #Calculate the minimum number of packages of hot dog buns
    minBuns = math.ceil(total / hotDogBuns)

    #Display the results
    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

def getTotalHotDogs():
    #Find out number of people attending the cookout
    people = int(input("Enter the number of people attending the cookout: "))

    #Get the number of hot dogs for each person
    hotDogs = int(input("Enter the number of hot dogs for each person: "))

    #Calculate the total number of hot dogs that need to be purchased
    total = people * hotDogs
    return total

def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    #Display the minimum packages of hot dogs needed
    print("Minimum packages of hot dogs needed:", minDogs)

    #Display the minimum packages of buns needed
    print("Minimum packages of hot dog buns needed:", minBuns)

    #Display how many hot dogs are left over
    print("Hot dogs left over:", dogsLeft)

    #Display how many of hot dog buns are left over
    print("Hot dog buns left over:", bunsLeft)

if __name__ == "__main__":
    main()