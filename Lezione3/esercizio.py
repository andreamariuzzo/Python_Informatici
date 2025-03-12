# Esercizio 1 Stampa il tuo nome e cognome in console, nel terminale. Specifica 2 variabili distinte
nome = "Andrea"
cognome = "Mariuzzo"

print(nome, cognome)


# Esercizio 2 Calcola l'area e il perimetro di un rettangolo avente base = 5.7 e altezza = 6.2
base = 5.7
altezza = 6.2

perimetro = 2 * (base + altezza)
area = base * altezza

print("Perimetro:", perimetro)
print("Area:", area)



# Esercizio 3 Calcola l'area e il perimetro di un triangolo rettangolo avente lato1 = 9, lato2 = 12, lato3 = 15
lato1 = 9
lato2 = 12
lato3 = 15

# Calcolo del perimetro
perimetroTriangolo= lato1 + lato2 + lato3

# Calcolo dell'area
areaTriangolo= (lato1 * lato2) / 2





# Esercizio 4 Calcola l'area e il perimetro di un cerchio di raggio 8.7
import math
raggio = 8.7

# Calcolo del perimetro (circonferenza)
perimetroCerchio= raggio * 2 * math.pi  

# Calcolo dell'area usando l'operatore **
areaCerchio_metodo1 = math.pi * (raggio ** 2)

# Calcolo dell'area usando la funzione pow()
areaCerchio_metodo2 = math.pi * pow(raggio, 2)

print("Perimetro del cerchio:", perimetroCerchio)
print("Area del cerchio (metodo 1):", areaCerchio_metodo1)
print("Area del cerchio (metodo 2):", areaCerchio_metodo2)