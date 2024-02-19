print("Hello welcome to our coffee shop")

name = input('What is your name?')

print("Hi",name,",What would you like today?")

print()

# Get the number of coffees and muffins from user
coffee_count = int(input('Enter the number of coffee cups: '))
muffin_count = int(input('Enter the number of muffins: '))

# Define prices
coffee_price = 5.00
muffin_price = 4.00

# Calculate Subtotal
subtotal = (coffee_count * coffee_price) + (muffin_count * muffin_price)

# Calculate tax (6%)
tax = 0.06 * subtotal

# Calculate Total
total = subtotal + tax
print('------------------')

print('Welcome to my Coffee shop')

print('Number of coffees bought?')

print(coffee_count)

print('Number of muffins bought?')

print(muffin_count)

print('------------------')

print()

print('------------------')

print('Coffee and Muffin shop reciept')

print()

print((coffee_count),'coffee','at $5 each:$',(coffee_price * coffee_count))

print((muffin_count),'muffin','at $4 each:$',(muffin_price * muffin_count))


# Display the results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (6%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

print('------------------')