#Matchlen
def matchlen(s, length):
    return (s * (length//len(s)+1))[:length]

#Intro
choice = input("Do you want to encrypt (e) or decrypt (d) a word?: ")
print("Input a word and a key: ")
palabraoriginal = input("Word: ")
clave = input("Key: ")

#abc
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Contar
long = len(palabraoriginal)

#Lista
lista_palabra = list(palabraoriginal)
lista_clave = list(clave)
lista_resultado = []

#ClaveLongitud
lista_clavelongitud = matchlen(lista_clave, long)

#Zippeado
zipped = list(zip(lista_palabra, lista_clavelongitud))

if choice == "e" or choice == "E":
    for n in range(0, long):
        indiceN=int((abc.index((zipped[n])[0]))+(abc.index((zipped[n])[1])))
        if indiceN > 26:
            indiceN = indiceN - 26
            lista_resultado.append(abc[indiceN])
        if indiceN > 52:
            indiceN = indiceN - 52
            lista_resultado.append(abc[indiceN])
        else:
            indiceN = indiceN - 26
            lista_resultado.append(abc[indiceN])
    print("The encrypted word is:", "".join(lista_resultado))

else:
    for n in range(0, long):
        indiceN=int((abc.index((zipped[n])[0]))-(abc.index((zipped[n])[1])))
        if indiceN > 26:
            indiceN = indiceN - 26
            lista_resultado.append(abc[indiceN])
        if indiceN > 52:
            indiceN = indiceN - 52
            lista_resultado.append(abc[indiceN])
        else:
            lista_resultado.append(abc[indiceN])
    print("The decrypted word is:", "".join(lista_resultado))
