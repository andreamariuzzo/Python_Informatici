# L'AND logico (&&) mi permette di unire più condizioni. Vuol dire che ho bisogno che tutte le condizioni siano valide affinchè tutte le condizioni siano 

#Stefano compie 18 anni, da oggi può accere al club dei programmatori, ma deve avere un invito

etaStefano = 17
invito = False

if etaStefano >= 18 and invito:
    print("Benvenuto nel club dei programmatori")
elif etaStefano < 18 and invito:
    print("Mi dispiace, non hai ancora 18 anni. Anche se hai un invito non puoi accedere al club dei programmatori")
elif etaStefano >= 18 and not invito: # Il NOT logico nega la condizione
    print("Mi dispiace, non hai un invito. Anche se hai 18 anni non puoi accedere al club dei programmatori")
else:
    print("Mi dispiace, non puoi accedere al club dei programmatori, non hai 18 anni e non hai un invito")

# Continua il codice chiedendo il suo nome, l'età e se ha un invito

nome = input("Qual è il tuo nome? ")
eta = int(input("Quanti anni hai? "))
invito = input("Hai un invito? ")

if eta >= 18 and invito == "si":
    print("Benvenuto nel club dei programmatori")
elif eta < 18 and invito == "si":
    print("Mi dispiace, non hai ancora 18 anni. Anche se hai un invito non puoi accedere al club dei programmatori")
elif eta >= 18 and invito == "no":
    print("Mi dispiace, non hai un invito. Anche se hai 18 anni non puoi accedere al club dei programmatori")
else:
    print("Mi dispiace, non puoi accedere al club dei programmatori, non hai 18 anni e non hai un invito")    