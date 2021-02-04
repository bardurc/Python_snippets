# Printing current date and time

# Necessary import
from datetime import datetime

####################################################
# Print current date and time with default formatting
print(datetime.now())
# output format = [year]-[month]-[day] [hour]:[minute]:[second].[microsecond]
# output example = 2021-02-04 10:39:31.506319

####################################################

# Define format of date and time using "strftime"
# strftime uses %-formatting as a way to decide how you want your date to be formatted
# See full list here: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


# Print current date and time with "strftime"-formatting
datetime_now = datetime.now()
print(datetime_now.strftime('%d/%m-%Y %H:%M:%S'))
# Example output = 04/02-2021 10:45:14

# You can change the delimiters to fit your needs
datetime_now = datetime.now()
print(datetime_now.strftime('%d-%m-%Y %H:%M:%S'))
# Example output = 04-02-2021 10:45:14
datetime_now = datetime.now()
print(datetime_now.strftime('%d-%m-%Y %H.%M.%S'))
# Example output = 04-02-2021 10.45.14

# You can exclude the date and only print the current time
datetime_now = datetime.now()
print(datetime_now.strftime('%H:%M:%S'))
# Example output = 10:45:14
