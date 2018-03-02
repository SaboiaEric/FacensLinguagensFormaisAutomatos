#Teacher exercise

word = input("Write:")
state = 0

for c in word:
  if(state == 0):
    if(c == '0'):
      state = 0
    elif(c == '1'):
      state = 1
    else:
      state =-1
      break
  else:
    if(c == '0'):
      state = 0
    elif (c == '1'):
      state = 1
    else:
      break

if(state == 0):
  print('Sucess')
else:
  print('Error')