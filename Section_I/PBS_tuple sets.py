"""
Python Data Structure, tuple and sets
"""
"""
tuple and set are two basic structures with different features to list.
"""

# tuple is very alike list, but tuple is immutable
person_list = ['Jon Dow', '06-04-2000', 'Male', 'U.S.A']
person_tuple = ('Jon Dow', '06-04-2000', 'Male', 'U.S.A')
person_list[0] = 'Allan Lee'  # ['Allan Lee', '06-04-2000', 'Male', 'U.S.A']
person_tuple[0] = 'Allan Lee'  # tuple' object does not support item assignment

# set
countries_1 = {'China', 'Korea', 'Japan', 'Turkey', 'Singapore', 'Russia', 'Japan'}
countries_2 = {'UK', 'Germany', 'France', 'Spain', 'Italy', 'Russia', 'Turkey'}

print(countries_1)  # sets will drop duplicated elements automatically
count_inter = countries_1.intersection(countries_2)  # {'Russia', 'Turkey'}
count_1_diff = countries_1.difference(countries_2)  # {'China', 'Japan', 'Korea', 'Singapore'}
count_2_diff = countries_2.difference(countries_1)  # {'France', 'Germany', 'Italy', 'Spain', 'UK'}
countries_new = countries_1.union(countries_2)  # merge two sets into 1 and without duplicates





