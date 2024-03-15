#Sofia Chiang
#CIS129_SofiaChiang_Lab5.py
#03/15/2024
#This program calculates total number of bottles and total payout


# Declare variables
total_bottles = 0
today_bottles = 0
counter = 1
NBR_of_days = 7
total_payout = 0
keep_going = 'y'

# Initialize keep_going to 'y'
while keep_going == 'y':
    total_bottles = 0
    counter = 1

    # Get number of bottles for each day of the week and add them all together
    while counter <= 7:
        today_bottles = int(input(f'Enter number of bottles for day #{counter}: '))
        total_bottles += today_bottles
        counter += 1

    # Calculate the total payout
    total_payout = total_bottles * 0.10

    # Display number of bottles and payout
    print(f'The total number of bottles collected is: {total_bottles}')
    print(f'The total payout is: ${total_payout:.2f}')

    # Ask user if they'd like to continue
    keep_going = input('Would you like to enter another week’s worth of data? (Enter y or n): ')