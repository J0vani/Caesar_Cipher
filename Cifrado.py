## Equipo ##
## Karina Lizbeth Pérez López ##
## Jovani Reyes Benitez ##


from io import open
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

txtFile = open('File.txt','r', encoding="utf8")
fileContent = txtFile.readlines()
txtFile.close()

plain_text = ""
for f in fileContent:
    plain_text += f.replace("\n", " ").upper()

print("Texto Claro: ",plain_text)
alphabet = "abcdefghijklmnñopqrstuvwxyz1234567890"

key = int (input("Llave: "))

encrypted_text = ""

for pt in plain_text:
        if pt == pt.upper():
            if pt.lower() in alphabet:
                encrypted_text += alphabet[((alphabet.index(pt.lower()) + key) % (len(alphabet)))].upper()
                print(encrypted_text)
            else:
                if pt == " ":
                    encrypted_text += pt
                else:
                    encrypted_text += ""
        else:
            if pt in alphabet:
                encrypted_text += alphabet[((alphabet.index(pt) + key) % (len(alphabet)))]
            else:
                if pt == " ":
                    encrypted_text += pt
                else:
                    encrypted_text += ""
print("Texto Cifrado: ",encrypted_text)

#c = Counter(encrypted_text)
#plt.bar(*zip(*c.most_common()), width=.5, color='g')
letters = ['ABCDEFGHIJKLMNÑOPQRSTUVWXYZ']
lcount = dict([(l, 0) for l in letters])

for l in open(fileContent).read():
    try:
        lcount[l.upper()] += 1
    except KeyError:
        # Ignore characters that are not letters
        pass
# The total number of letters
norm = sum(lcount.values())

fig = plt.figure()
ax = fig.add_subplot(111)
# The bar chart, with letters along the horizontal axis and the calculated
# letter frequencies as percentages as the bar height
x = range(37)
ax.bar(x, [lcount[l]/norm * 100 for l in letters], width=0.8,
       color='g', alpha=0.5, align='center')
ax.set_xticks(x)
ax.set_xticklabels(abc)
ax.tick_params(axis='x', direction='out')
ax.set_xlim(-0.5, 25.5)
ax.yaxis.grid(True)
ax.set_ylabel('Letter frequency, %')
plt.show()

outputFile = open('FileC.txt','w',encoding="utf8")
outputFile.write(encrypted_text)
outputFile.close()

