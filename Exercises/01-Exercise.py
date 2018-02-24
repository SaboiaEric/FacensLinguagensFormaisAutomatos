import re
#inicialLetra = 'S' 
alfabeto = ['a','b']
#conversoes = ['S','AA','-','A','aB','Ba','-','B','Bb','b']

def pertenceLinguagem(palavra):
  print("\nChecking if word there is in language")
  for char in palavra:
    if(char not in alfabeto): return False

  if(not verificaGramatica(palavra)): return False
    
  return True
    
def verificaGramatica(palavra):
  answer = re.search(r'^b*((ab+){2})$', palavra)
  if answer: return True
  
  return False


word = input('Go!! Write the word: ')
resultado = pertenceLinguagem(word)
if resultado: print('Pertence')
else: print('Nao Pertence')