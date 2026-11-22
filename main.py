import numpy as np

notes = [12,15,14,18,10,16]

def calcul_moyenne(data):
    return np.mean(data)

def calcul_variance(data):
    return np.var(data)

def calcul_ecart_type(data):
    return np.std(data)

def calcul_mediane(data):
    return np.median(data)

def calcul_somme(data):
    return np.sum(data)


if __name__ == "__main__":
    print("Moyenne :", calcul_moyenne(notes))
    print("Variance :", calcul_variance(notes))
    print("Ecart-type :", calcul_ecart_type(notes))
    print("Médiane :", calcul_mediane(notes))
    print("Somme :", calcul_somme(notes))
