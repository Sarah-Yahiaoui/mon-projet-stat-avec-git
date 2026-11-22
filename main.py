import numpy as np

notes = [12,15,14,18,10,16]

moyenne = np.mean(notes)
print("Moyenne est:", moyenne)

variance = np.var(notes)
print("variance est:", variance)

ecart_type =np.std(notes)
print("ecart type est :", ecart_type)