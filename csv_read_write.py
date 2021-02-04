# Necessary import statement
import csv


my_list_of_lists = [[1,2,3,4],[11,22,33,44],[111,222,333,444]]

# Write to CSV
with open('test_output.csv', 'w', newline = '', encoding = 'utf-8') as f:
    # If "delimiter" is not set it defaults to comma. I just like to add the parameter to be explicit
    writer = csv.writer(f, delimiter = ',')
    
    # "writer.writerow" writes a single row
    # Can be used as a simple way of writing headers in a csv file
    writer.writerow(['no1','no2','no3','no4'])
    
    # "writer.writerows" writes multiple rows. Similar to "for e in my_list_of_lists: writer.writerow(e)"
    writer.writerows(my_list_of_lists)

# This writes the following in a csv named "test_output.csv":
'''
        no1,no2,no3,no4
        1,2,3,4
        11,22,33,44
        111,222,333,444
'''
