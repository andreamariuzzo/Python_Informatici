nomeUtente = "Andrea Mariuzzo"

presentazione = "Ciao, " + nomeUtente + " benvenuto nella calcolatrice scema!"
print(presentazione)

numero1 = 42.3
numero2 = 6.4

#calcolare le 4 operazioni di base

somma = numero1 + numero2
print("La somma vale: ", somma)

prodotto = numero1 * numero2
print("Il prodotto vale: ", prodotto)

sottrazione = numero1 - numero2
print("La sottrazione vale: ", sottrazione)

divisione = numero1 / numero2
print("La divisione vale: ", divisione)

# Elevare un numero alla potenza
# eleviamo alla potenza 2 i numeri

potenza1 = numero1 ** 2
potenza2 = numero2 ** 2
print("la potenza del primo numero vale: ", potenza1)
print("la potenza del secondo numero vale: ", potenza2)

# Calcolare la radice quadrata utilizzando potenza
radice1 = numero1 ** (1/2)
radice2 = numero2 ** (1/2)

print("la radice quadrata del primo numero vale: ", radice1)
print("la radice quadrata del secondo numero vale: ", radice2)

numeroProva = 2
elevazioneNeg = numeroProva ** -2
print(elevazioneNeg)

numeroProva2 = -2
elevazionePos = numeroProva2 ** 3
print(elevazionePos)


# Metodo 2
numero3 = 4 
#elevo questo numero alla potenza 2
potenza3 = pow(numero3, 2)
print("la potenza di numero 3 vale: ", potenza3)    

# Calcolo radice di 4 con sqrt
# Importiamo la libreria math
import math
radice3 = math.sqrt(numero3)
print("la radice di numero3 vale: ", radice3)
