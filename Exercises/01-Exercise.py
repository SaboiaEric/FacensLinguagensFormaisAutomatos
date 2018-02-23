inicialLetra = 'S' 
alfabeto = ['a','b']
conversoes = ['S','AA','-','A','aB','Ba','-','B','Bb','b']

def pertenceLinguagem(palavra):
  for char in palavra:
    if(char not in alfabeto):
      return False
  
  if(not verificaGramatica(palavra)):
    return False
    
  return True
    
def verificaGramatica(palavra):
  #implementHere
  
  return False

resultado = pertenceLinguagem('aa')
if resultado:
  print('Pertence')
else:
  print('Nao Pertence')