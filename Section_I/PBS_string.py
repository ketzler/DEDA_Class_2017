"""
Python Basic Syntax, string
"""

"""
String is a basic type in python, it's common used and very powerful
"""

welcome_list = ['Welcome', 'to', 'Python', 'World.', 'It\'s', 'Amazing']
# using back slash to escape the single quote.

# using for loop to iterate all elements in the list.
for word in welcome_list:
    print(word)

# a string is also an object, using the join method to connect all the words in the list.
welcome_sentence = ' '.join(welcome_list)

# slicing string by indices.
welcome_sliced = welcome_sentence[0:10]
# try changing the indices to negative.

# see other methods of string object, like:
welcome_lower_case = welcome_sentence.upper()
# by using dir() function, or help() function
dir(str)
# or a str instance
dir(welcome_lower_case)
# likewise,
help(str)

# formatting string
greeting = 'Hallo'
name = 'Jon'
# using format method
welcome_jon = '{}, {}. '.format(greeting, name.upper()) + welcome_sentence
# using f string, you can write variable name into brackets, directly.
welcome_jon_f = f'{greeting}, {name.upper()}. '+ welcome_sentence








