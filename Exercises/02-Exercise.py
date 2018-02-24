import re

def checkIfWordIsInLanguage(word):
  answer = re.search(r'^[01]+0$', word)
  if answer: return True
  
  return False


word = input('Go!! Write the word: ')
result = checkIfWordIsInLanguage(word)
if result: print('Yes')
else: print('No')