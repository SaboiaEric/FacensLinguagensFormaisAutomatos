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
dictionary[0] = {'0':1,'1':0}
dictionary[1] = {'1':0, '1':2,'0':1}
dictionary[2] = {'0':1, '0':3,'1':2}
dictionary[3] = {'1':2,'1':4,'0':3}
dictionary[4] = {'0':3,'0':4,'1':4}

result = checking(word)

if result: print('Yes')
else: print('No')