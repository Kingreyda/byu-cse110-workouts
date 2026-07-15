"""
Author: Olaribigbe King David
Purpose: Meal Calculator

For my creativity, I added an optional tip feature that allows customers
to include a tip before the final bill is calculated.
"""

#LOCALISATION SECTION
import locale
currency_symbol = "$"

locale_value = "en_US.UTF-8"
locale.setlocale(locale.LC_ALL, locale_value)


#MEAL SECTION
child_price = float(input("\nWhat is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))

child_no = int(input("How many children are there? "))
adult_no = int(input("How many adults are there? ")) 

child_total = child_price * child_no
adult_total = adult_price * adult_no 

subtotal = child_total + adult_total
subtotal_formatted = locale.currency(subtotal, grouping=True, symbol=True)

print(f"\nSubtotal: {subtotal_formatted}")


#TAX SECTION
tax_rate = float(input("\nWhat is the sales tax rate? "))
sales_tax = (tax_rate / 100) * subtotal

sales_tax_formatted = locale.currency(sales_tax, grouping=True, symbol=True)
print(f"Sales Tax: {sales_tax_formatted}")

total = sales_tax + subtotal


#CREATIVITY SECTION - "Tip"
tip_amount = 0

tip = input("\nWould you like to drop a tip? (yes or no): ")

if tip.lower() == "yes":
    tip_amount = float(input("\nPlease input amount: "))

tip_formatted = locale.currency(tip_amount, grouping=True, symbol=currency_symbol)
print(f"\nTip: {tip_formatted}")

overall_total = total + tip_amount
overall_total_formatted = locale.currency(overall_total, grouping=True, symbol=currency_symbol)

print(f"Total: {overall_total_formatted}")


#PAYMENT SECTION
payment_amount = float(input("\nWhat is the payment amount? "))
change = payment_amount - overall_total

change_formatted = locale.currency(change, grouping=True, symbol=currency_symbol)
print(f"\nChange: {change_formatted}")
