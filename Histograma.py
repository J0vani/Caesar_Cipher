## Equipo ##
## Karina Lizbeth Pérez López ##
## Jovani Reyes Benitez ##

import pandas
from io import open

txtFile = open( 'FileC.txt','r')
fileContent = txtFile.readlines()
txtFile.close()

# Replace returns by spaces
encrypted_text = ""
for fc in fileContent:
    encrypted_text += fc.replace("\n", " ").upper()

from collections import Counter
a = encrypted_text
letter_counts = Counter(a)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar')