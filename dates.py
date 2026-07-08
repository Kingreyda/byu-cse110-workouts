from datetime import datetime
datetime_value = datetime.now()

datetime_format = "%A-%m-%B-%Y %I:%p"
datetime_formatted = datetime_value.strftime(datetime_format)

print(datetime_formatted)
