# Content of 'test_output.csv':
'''
        no1,no2,no3,no4
        1,2,3,4
        11,22,33,44
        111,222,333,444
'''

# Necessary import statement
import csv

##################################################

# Print only first row from CSV-file
with open('test_output.csv', 'r', newline = '', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    # "header = next(f)" skips the first row and adds the first row to the variable "header"
    header = next(f)
    print(header)

# Output
'''
        no1,no2,no3,no4
'''

##################################################

# Print all rows from CSV-file
with open('test_output.csv', 'r', newline = '', encoding = 'utf-8') as f:
    # If "delimiter" is not set it defaults to comma
    reader = csv.reader(f)
    for e in reader:
        print(e)

# Output
'''
        ['no1', 'no2', 'no3', 'no4']
        ['1', '2', '3', '4']
        ['11', '22', '33', '44']
        ['111', '222', '333', '444']
'''

##################################################

# Print specific entry in each row from CSV-file
with open('test_output.csv', 'r', newline = '', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for e in reader:
        # print only the second entry in each row (remember count starts from 0)
        print(e[1])

# Output
'''
        no2
        2
        22
        222
'''
