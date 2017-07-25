import unittest;

"""
Write a function called longest which will take a string of
space separated words and will return the longest one.

For example:

longest("This is Andela") => "Andela"
longest("A") => "A"

"""
def longest(word):
    new_word = word.split(' ')

    return max(new_word, key = len)




class Test(unittest.TestCase):
     def test_longest_word(self):
            sentence = "This is Andela"
            self.assertEqual('Andela', longest(sentence))

     def test_one_word(self):
            sentence = "This"
            self.assertEqual("This", longest(sentence))
