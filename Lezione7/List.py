# Le liste servono per trattenere più informazioni
# sonp dei contenitori di elementi simili tra loro. Ovvero sono dei contenitori omogenei, vuol dire che contengono lo stesso tipo di dati.
# Possono essere numeri, stringhe, ecc.

miaLista = ["mele", "pesca", "banane", "kiwi" ]
print(miaLista)
print(miaLista[0]) 
print(miaLista[1]) 
print(miaLista[2]) 
print(miaLista[3]) 
print(len(miaLista)) 

#Il ciclo FOR è adatto a stampare ogni songolo elemento della lista

for frutto in miaLista:
    print(frutto)

#Esempio, fornisco una lista di voti. Tutte le volte che insufficiente stampo un avviso
voti = [100, 50, 25, 85, 20]

for voto in voti:
    if voto <= 60:
        print("Voto:", voto, "Insufficiente")
    else:
        print("Voto:", voto, "Sufficiente")