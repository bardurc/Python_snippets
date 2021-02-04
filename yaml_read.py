# Reading data from yaml file

# Content of example yaml file:
'''
        ---
        Example Entity: example.com
        Microsoft: microsoft.com
        Google: google.com
'''
# The key is everything before the ":" and the value is everything after the ":"
# In the script the key and value are retrived in the "for k, v in data.items()" line

# Necessary import (install with "python -m pip pyyaml")
import yaml


with open('domains.yaml', encoding='utf-8') as f:
    # yaml.load() loads data from the yaml file into a dictionary
    # The "Loader=yamlBaseloader" is a way to load yaml safely
    # See https://msg.pyyaml.org/load for more details
    data = yaml.load(f, Loader=yaml.BaseLoader)
    for k, v in data.items():
        print(f'k: {k}')
        print(f'v: {v}')
        print('************')

# Output
'''
        k: Example Entity
        v: example.com
        ************
        k: Microsoft
        v: microsoft.com
        ************
        k: Google
        v: google.com
        ************
'''
