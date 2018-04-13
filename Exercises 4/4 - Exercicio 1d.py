import re

dictionary = {}
finalState = [6]


def checking(word):
    print(word)
    state = 0
    for char in word:
        try:  
            state = dictionary[state][char]
        except:
            return False  
    if state in finalState:
        return True
    
    return False


word = input('Go!! Write the word: ')
dictionary[0] = {'0':2,'1':1}
dictionary[1] = {'0':5,'1':4}
dictionary[2] = {'0':3,'1':5}
dictionary[3] = {'0':3, '0':6,'1':6}
dictionary[4] = {'0':4,'1':4}
dictionary[5] = {'0':6}
dictionary[6] = {'0':6}

result = checking(word)

if result: print('Yes')
else: print('No')