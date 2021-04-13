# Purpose: Use dictionary to count occurrence of something
# The example counts occurrence of each character in a string
# To sort the dictionary, use the function in sort_dict.py
#   - https://github.com/bardurc/my_snippets/blob/5d58fbed734a647b49d84e761e21e212d4ef12f4/dictionaries/sort_dict.py

my_str = 'This is just a sample string for the script to count characters'

character_occurrence = {}

# Iterate over each character in my_str
for character in my_str:
    # get() method adds character to the dictionary as a key
    # If character does not already exist in the dictionary it gets the value 0
    # 1 is then added to the value
    # If character already exists in the dictionary, 1 is added to whatever value it already has    
    character_occurrence[character] = character_occurrence.get(character, 0) + 1

#############################################

# Running the following
for k,v in character_occurrence.items():
    print(k, v)

# Gives the following output
'''
    T 1
    h 3
    i 4
    s 7
      11
    j 1
    u 2
    t 7
    a 4
    m 1
    p 2
    l 1
    e 3
    r 5
    n 2
    g 1
    f 1
    o 3
    c 4
''''
