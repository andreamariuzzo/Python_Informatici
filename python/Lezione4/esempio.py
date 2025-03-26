# Esempio dichiarazione e uso variabili

print("Scrivi il tuo nome, caro utente!")

# Per poter acquisire qualcosa che digita l'utente, usiamo la funzione input()
# nomeUser = "Andrea"
nomeUser = input()
print("Benvenuto" , nomeUser)

# Facciamo la stessa cosa in moodo più veloce passando come argomento all'input una frase
# Funzione (argomento) --> tutto questo si chiama FIRMA del METODO

cognomeUser = input("Scrivi il tuo cognome ")
print("Il tuo cognome è", cognomeUser)

print("-------NUMERI-------")
# ATTENZIONE: Tutto ciò che recupero da un utente è considerato una stringa, un testo. Per poter fare calcoli devo usare Type Casting ovvero forzare quella variabile a diventare un numero e non una stringa

# int() trasforma una stringa in un numero intero
num1 = int(input("Scrivi un numero "))
num2 = int(input("Scrivi un altro numero "))
somma = num1 + num2
print("La somma è", somma)