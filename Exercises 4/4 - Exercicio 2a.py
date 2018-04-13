import re

dictionary = {}
finalState = [0]



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
dictionary[0] = {'b':0,'a':1}
dictionary[1] = {'b':2,'a':1}
dictionary[2] = {'a':3}
dictionary[3] = {'b':0}

result = checking(word)

if result: print('Yes')
else: print('No')