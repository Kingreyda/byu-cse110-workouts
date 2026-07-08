#My Tryout
import locale

money_value = 20099876.00
currency_symbol = "£"

locale_value = "en_GB.UTF-8"
locale.setlocale(locale.LC_ALL, locale_value)

money_formated = locale.currency(money_value, grouping=True, symbol=currency_symbol)
print()
print(money_formated)


#The Homework
money_value = 1245.60
currency_symbol = "USD$"

locale_value = "en_US.UTF-8"
locale.setlocale(locale.LC_ALL, locale_value)

money_formatted = locale.currency(money_value, grouping=True, symbol= currency_symbol)
print (money_formatted)