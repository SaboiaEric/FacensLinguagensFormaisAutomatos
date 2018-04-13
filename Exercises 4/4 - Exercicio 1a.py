import re

dictionary = {}
finalState = [3]



def checking(word):
    print(word)
    state = 0
    for letra in word:
        try:  
            state = dictionary[state][letra]
        except:
            return False  
    if state in finalState:
        return True
    
    return False


word = input('Go!! Write the word: ')
dictionary[0] = {'0': 0, '1': 0, '1': 1}
dictionary[1] = {'0': 1, '1': 1, '1': 2}
dictionary[2] = {'0': 2, '1': 2, '1': 3}
dictionary[3] = {'0': 3, '1': 3}

result = checking(word)

if result: print('Yes')
else: print('No')