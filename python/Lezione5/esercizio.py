# Chiedere all'utente quanto ha guadagnato questo mese (utilizza un valore con la virgola)
#Se l'utente ha guadaganto più di 1000 euro, scrivere "Bravo! Hai guadagnato bene!"
#Calcolare il saldo su 10000 (guadagno 1500, incasso ( 1500 + 10000) = 10500)

#Se l'utente ha guadagnato meno di 1000 euro, scrivere "Mi spiace, questo mese hai guadagnato poco", calcolare il saldo su 10000 euro
#Se l'utente ha guadaganto 0 stampare "Questo mese non hai guadagnato nulla", Calcolare il saldo 
#Se l'utente è andato in perdita scrivere: " Questo mese hai perso soldi", calcolare il saldo

saldo = 10000
guadagno = float(input("Quanto hai guadagnato questo mese? ")) #Chiedo all'utente quanto ha guadagnato questo mese
saldo = saldo + guadagno 

if guadagno >= 1000:
    print("Bravo! Hai guadagnato bene!")
    1500 
elif guadagno < 0:
    print("Questo mese hai perso soldi")
elif guadagno == 0:
    print("Questo mese non hai guadagnato nulla")
else:
    print("Mi spiace, questo mese hai guadagnato poco")

print("Il tuo saldo è di ", saldo, " euro") #Stampo il saldo finale



