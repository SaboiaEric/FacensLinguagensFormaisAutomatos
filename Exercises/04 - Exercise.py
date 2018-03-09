# https://regex101.com/

import re

word = input("Let's go: ")



#m = re.compile('^[0-9]+$').match(word) is not None

#m = re.compile('([0-9]+[A-z]+)(?0)?').match(word)



## Just numbers 

## m = re.compile('^[0-9]+$').match(word) is not None



## Just chars 

## m = re.compile('^[A-z]+$').match(word) is not None



## Just Alphanumeric, started with numbers and finished with chars

m = re.compile('^([0-9]+[A-z]+)$').match(word) is not None



## Just pair number in binary

#m = re.compile('^[01]*0$').match(word) is not None



## Just odd number in binary

#m = re.compile('^[01]*1$').match(word) is not None

print(m)
