import re

alphabet = ['a','b']

def CheckingLanguage(word):
  print("\nChecking if the word there is on language")
  for char in word:
    if(char not in alphabet): return False

  #Checking the grammar
  answer = re.search(r'^b*((ab+){2})$', word)
  if answer: return True

  return False
    

word = input('Go!! Write the word: ')
result = CheckingLanguage(word)
if result: print('Yes')
else: print('No')