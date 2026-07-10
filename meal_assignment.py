"""
Author: Olaribigbe King David
Purpose: Meal Calculator
"""

#MEAL SECTION
child_price = float(input("\nWhat is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))

child_no = int(input("How many children are there? "))
adult_no = int(input("How many adults are there? ")) 

child_total = child_price * child_no
adult_total = adult_price * adult_no 

subtotal = child_total + adult_total
print(f"\nSub-total: {subtotal}")

#TAX SECTION
tax_rate = float(input("\nWhat is the sales tax rate? "))
sales_tax = (tax_rate / 100) * subtotal