from operator import and_
from functools import reduce

def is_isogram(word):
    assert (type(word) == str),"Argument should be a string"
    if word == " ":
      return (word, False)
    word = word.replace(" ","")
    new_word = list(word)
    occurList = []
    for char in new_word:
        if new_word.count(char) == 1:
            occurList.append(True)
        else:
            occurList.append(False)
    return (word,reduce(and_, occurList))



#word = ' '
#print(is_isogram(word))
