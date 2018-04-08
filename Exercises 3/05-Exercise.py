import re

def checkIfWordIsInLanguage(word):
  answer = re.findall(r'[01]+[1$]', word)
  print(answer)
  if answer: return True
  
  return False


word = input('Go!! Write the word: ')
result = checkIfWordIsInLanguage(word)
if result: print('Yes')
else: print('No')