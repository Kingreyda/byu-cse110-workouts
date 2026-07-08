from datetime import datetime
datetime_value = datetime.now()

datetime_format = "%d-%m-%Y %H:%M"
datetime_formatted = datetime_value.strftime(datetime_format)

print(datetime_formatted)