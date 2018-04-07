import re

def CheckThePhoneNumber(n):
  answer = re.search(r'^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$', n)
  if answer: return True

  return False

print('Format (**) *****-****')
number = input('Go!! Write the number: ')
result = CheckThePhoneNumber(number)
if result: print('Yes')
else: print('No')