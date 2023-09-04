# Todo: Tip Calculator

# Prgram Instrustion
#1. The program should ask the user to enter the charge for the food.
#2. It should then calculate the amounts of an 18 percent tip and  7 percent sales tax on the charge of the food and display each of these amounts.
#3. Finally, it should add everything together and display the charge of the food plus tip and sales tax.



# ask the user to enter the charge for the food.
charge = input("Please Enter Charge For the food/drink: ")

# Calculate 18 Percent tips 
tip = (18 * int(charge)) / 100
print("Tip = $" + str(tip))

# Calculate 7 Percent Sales tax
tax = (7 * int(charge)) / 100
print("Sales tax = $" + str(tax))

#Finally, it should add everything together and display the charge of the food plus tip and sales tax.
total = tip + tax + int(charge)
print("Grand total = $" + str(total))