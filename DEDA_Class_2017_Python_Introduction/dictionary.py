
"""
Data Structure Dictionary
"""

"""
Like a real dictionary, dict type is form by 2 parts, a unique key and values for a key.
"""

# initial a dict
profile = {'name': 'Anna', 'birth': '10-05-2000', 'gender': 'female', 'height': 1.70}

# find the value by using the key
print(profile['name'])  # 'Anna'

# get all the keys and put into a list
keys = list(profile.keys())  # ['name', 'birth', 'gender', 'height']
# get all values and put into a list
values = list(profile.values())  # ['Anna', '10-05-2000', 'female', 1.7]
# get all key-value pairs and put into a list
key_value = list(profile.items())

# add a key with value
profile['weight'] = 55
# change value of a key
profile['name'] = 'Yoki'
# alter multiple keys and values at a time
profile.update({'birth': '01-10-2001', 'tel': '123-312'})

# loop with key and vlaue
for key, value in profile.items():
    print(f'{key}: {value}')



