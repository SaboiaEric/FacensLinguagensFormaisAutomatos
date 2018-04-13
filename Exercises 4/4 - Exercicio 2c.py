import re

dictionary = {}
finalState = [4]



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
dictionary[0] = {'b':1,'a':2}
dictionary[1] = {'a':5,'b':1}
dictionary[2] = {'a':2,'b':3}
dictionary[3] = {'a':4,'b':3}
dictionary[4] = {'b':4}
dictionary[5] = {'b':4,'a':5}

result = checking(word)

if result: print('Yes')
else: print('No')