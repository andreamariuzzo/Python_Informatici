# Con il ciclo for non sono nei cicli indefiniti ma sono nei cicli definiti
# Dobbiamo usare un metodo chiamato range il quale stabilisce il numero di cicli da effettuare

# i sta per indice
for i in range(10): #ATT: il range (100) va da 0 a 9
    print(i)  

for i in range(15, 20): #ATT: il range (5, 10) va da 15 a 19
    print("La i vale", i)

for i in range(5, 60, 3): #ATT: il range (5, 60, 3) va da 5 a 59 con incremento di 3
    print("La i vale", i)

# Break e Continue
# Il break interrompe il ciclo
# Il continue permette di saltare un ciclo

# dato un set di numeri da 1 a 10, interrompi il ciclo quando il numero è 5
for x in range(1, 11):
    if x == 5:
     continue
    print(" La X vale" , x)