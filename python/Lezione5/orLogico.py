# Or Logico. In questo caso vale una condizione OPPURE l'altra affinchè quella globale sia true

# Esami: l'esame viene superato se passi lo scritto oppure l'orale

esameScritto = False
esameOrale = True

print("Professore Bravo")
if esameScritto or esameOrale:
    print("Hai superato l'esame")
else:
    print("Mi dispiace, non hai superato l'esame")


print("Professore Cattivo")
if esameScritto and esameOrale:
    print("Hai superato l'esame")
else:    
    print("Mi dispiace, non hai superato l'esame")