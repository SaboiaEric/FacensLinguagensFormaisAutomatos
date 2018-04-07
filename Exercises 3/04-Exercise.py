import re
## Serve para validar somente um IPv6 porque eu não entendi muito o enunciado :)
def CheckTheIPv6Address(n):
  answer = re.search(r'^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$', n)
  if answer: return True

  return False

print('Format (**) *****-****')
value = input('Go!! Write the value: ')
result = CheckTheIPv6Address(value)
if result: print('Yes')
else: print('No')