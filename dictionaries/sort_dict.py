# Function that sorts a dictionary by count (highest to lowest)
# key/value pairs in dictionary should be {item:count}
def sort_dict(dict_to_sort):
    dict_list = []
    for k,v in dict_to_sort.items():
        # Switch position of key/value so that it sorts by value and not key
        dict_list.append((v,k))
    return sorted(dict_list, reverse=True)

# Example dict
mydict = {'a':2,'b':4,'c':1,'d':2,'e':7,'f':4,'g':3,'h':2,'i':5}

# Running the following
for count, item in sort_dict(mydict):
    print(count, item)

# Gives the following output
'''
    7 e
    5 i
    4 f
    4 b
    3 g
    2 h
    2 d
    2 a
    1 c
''''
