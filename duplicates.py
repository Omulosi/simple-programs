""""
Write a function called remove_duplicates which will take one argument
called string. This string input will only have characters between a-z,
and should remove all repeated characters in the string.
Python

Return a tuple with two values:

A new string with only unique, sorted characters.
The total number of duplicates dropped.

For example:

remove_duplicates('aaabbbac') => ('abc', 5)
remove_duplicates('a') => ('a', 0)
remove_duplicates('thelexash') => ('aehlstx', 2)

"""
def remove_duplicates(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_str_list = list(string)
    original_length = len(new_str_list)

    unique_str_list = list(set(new_str_list))
    final = ''
    for elem in alphabet:
       if elem in unique_str_list:
            final = final+elem
            unique_str_list.remove(elem)

    new_length = len(final)

    duplicates_dropped = original_length - new_length

    return (final, duplicates_dropped)

    
print remove_duplicates('aaabbbac')
print remove_duplicates('a')
print remove_duplicates('thelexash')
print remove_duplicates('thisisateststring')
print remove_duplicates('letsseehowthisgoes')
print remove_duplicates('hiddenhiddenhiddenhaha')
