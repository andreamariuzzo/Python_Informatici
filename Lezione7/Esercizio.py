# scrivi un programma che stampa i numeri da 1 a 100
# Per i multipli di 3 stampa "BOOM"
# Per i multipli di 5 stampa "ZOOM"
# per i multipli di 3 e 5 stampa "BAZZINGA"



for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("BAZZINGA")
    elif i % 3 == 0:
        print("BOOM")
    elif i % 5 == 0:
        print("ZOOM")
    else:
        print(i)


# Data la segeunte lista di numeri
# 1. trova i numeri pari
# 2. calcola la somma dei numeri dispari
# 3. trova il numero massimo


numeri = [12, 3, 7, 24, 5, 18, 9, 10, 15, 2]
somma = 0
massimo = numeri[0] 


for i in numeri:
    if i % 2 == 0:
        print(i, "è pari")

for i in numeri:
    if i % 2 != 0:
        somma += i
        print(i, "La somma è", somma)


for numero in numeri:
    if numero > massimo:
        massimo = numero

print("Il numero massimo è:", massimo)





