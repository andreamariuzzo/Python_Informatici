#Implementare l'operazione di deposito contanti

nome = input ("Inserisci il tuo nome: ")
print("Ciao", nome)

saldo = 1000

print("Quanto vuoi depositare?")
deposito = int(input())


if deposito > 500:
    print("Mi spiace, non puoi depositare più di 500 euro")
else: 
    saldo += deposito
    print("Il tuo saldo attuale è di", saldo)

