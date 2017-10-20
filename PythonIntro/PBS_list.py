"""
Python Basic Syntax, list
"""
"""
Using list makes Python code simple.
"""

natr_language = ['English', 'German', 'Chinese']
prog_language = ['C++', 'Java', 'C#']

# how many elements in a list?
len(natr_language)  # 3

# adding elements into the list
# append() allows you to add 1 element at the end of the list
natr_language.append('Spanish')  # ['English', 'German', 'Chinese', 'Spanish']

# insert() allows you to add 1 element at arbitrary place
prog_language.insert(0, 'Python')  # ['Python', 'C++', 'Java', 'C#']


# extend() allows you to add multiple elements at the end of the list
python = ['python 2.7', 'python 3.6']
prog_language.append(python)  # ['Python', 'C++', 'Java', 'C#', ['python 2.7', 'python 3.6']]
minor_language = ['Japanese', 'Korean']
natr_language.extend(minor_language)  # ['English', 'German', 'Chinese', 'Spanish', 'Japanese', 'Korean']

# remove elements
prog_language.remove(python)  # ['Python', 'C++', 'Java', 'C#']
natr_language.pop(-1)  # 'Korean' pops out. ['English', 'German', 'Chinese', 'Spanish', 'Japanese']
del prog_language[-1]  # ['Python', 'C++', 'Java']

# reorder in list
numbers = [43, 11, 32, 95, 22]
numbers.reverse()  # [22, 95, 32, 11, 43]
numbers.sort()  # [11, 22, 32, 43, 95]
numbers.sort(reverse=True)  # [95, 43, 32, 22, 11]
sorted_number = sorted(numbers)  # sorted function can return a new list instead of altering the original list

# basic search in list
min_num = min(numbers)  # 11
max_num = max(numbers)  # 95
sum_num = sum(numbers)  # 203
index_num = numbers.index(32)   # 2

# iterate in list
for lang in prog_language:
    print(lang)
# iterate in list with index
for num, lang in enumerate(natr_language):
    print(f'{num}. {lang}')

# list to string
natr_language_str = ', '.join(natr_language)  # 'Spanish, Japanese, German, English, Chinese'
natr_language_new = natr_language_str.split(', ')  # ['Spanish', 'Japanese', 'German', 'English', 'Chinese']


# looping in the list. The basic syntax is:
# [func(ele) for func(ele) in a_list if func(ele)]
# For example:
people = [language + ' People' for language in natr_language_new if language.endswith('ese')]
# format number in list to 2 digit
num_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_seq_db = [format(num, '02d') for num in num_seq]

