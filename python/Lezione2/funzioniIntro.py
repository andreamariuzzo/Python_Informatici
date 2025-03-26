# Funzioni Built-in: sono funzioni che sono già presenti nel linguaggio di programmazione

print(" Anche print è una funzione built-in")

print("Inserici il tuo nome")
nome = input() #input è una funzione built-in che mi peremttte di inserire un valore e registrarlo in una variabile
print("Ciao", nome)

saldo = 1000

print("Quanto vuoi prelevare?")
prelievo = int(input()) #sto forzando l'input a essere un intero

#PICCOLO IF DI PROVA

if prelievo > 500:
    print("Mi spiace, non puoi prelevare più di 500 euro")
else:
    if prelievo > saldo:
        print("Non hai abbastanza soldi")
    else:
        saldo -= prelievo
        print("Il tuo saldo attuale è di", saldo)