print("Hello welcome to our coffee shop")

name = input('What is your name?')

print("Hi",name,",What would you like today?")

print()

# Get the number of items from user
coffee_count = int(input('Enter the number of coffee cups: '))
muffin_count = int(input('Enter the number of muffins: '))
latte_count = int(input('Enter the number of lattes: '))
tea_count = int(input('Enter the number of teas: '))

# Define prices
coffee_price = 5.00
muffin_price = 4.00
latte_price = 5.00
tea_price = 3.00

# Calculate Subtotal
subtotal = (coffee_count * coffee_price) + (muffin_count * muffin_price) + (latte_count * latte_price) + (tea_count * tea_price)

# Calculate tax (6%)
tax = 0.06 * subtotal

# Calculate Total
total = subtotal + tax
print('------------------')

print('Welcome to my Coffee shop')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('Number of coffees bought?')

print(coffee_count)

print('Number of muffins bought?')

print(muffin_count)

print('Number of lattes bought?')

print(latte_count)

print('Number of teas bought?')

print(tea_count)

print('------------------')

print()

print('------------------')

print('Coffee shop reciept')

print((coffee_count),'coffee','at $5 each:$',(coffee_price * coffee_count))

print((muffin_count),'muffin','at $4 each:$',(muffin_price * muffin_count))

print((latte_count),'latte','at $5 each:$',(latte_price * latte_count))

print((tea_count),'tea','at $3 each:$',(tea_price * tea_count))


# Display the results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (6%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print ()
print('------------------')
print ()
print('Thank you for coming in today! Hope to see you again soon.')
print()


print('------------------')
