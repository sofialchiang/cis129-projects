# Module 4 Lab-4
# Sofia Chiang (Arroyo)
# 02/26/2024
# This Program calculates the store's and employee's bonus based on the monthly sales and sales increase percentage


# Declare local variables
storeAmount =  0 # store bonus amount
empAmount =  0 # employee bonus amount
salesIncrease = 0 # percent of sales increase

# gets the monthly sales 
monthlySales = float(input('Enter the monthly sales $')) 
# gets the percent of increase in sales 
salesIncrease = float(input('Enter percent of sales increase: ')) 
salesIncrease = salesIncrease / 100 

# Determine store storeAmount
if monthlySales > 110000:
        storeAmount = 6000
elif monthlySales >= 100000:
        storeAmount = 5000
elif monthlySales >= 90000:
        storeAmount = 4000
elif monthlySales >= 80000:
        storeAmount = 3000
else:
        storeAmount = 0
        
# Determine Employee bonus
if salesIncrease >= 0.05:
        empAmount = 75
elif salesIncrease >= 0.04:
        empAmount = 50
elif salesIncrease >= 0.03:
        empAmount = 40
else:
        empAmount = 0
        
# prints the bonus information 
print('The store bonus amount is $', storeAmount) 
print('The employee bonus amount is $', empAmount) 
if storeAmount == 6000 and empAmount == 75: 
    print('Congrats! You have reached the highest bonus amounts possible!')
