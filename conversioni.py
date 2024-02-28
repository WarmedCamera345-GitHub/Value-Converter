# Importa la libreria con tutti i valori
import database

# Chiama la funzione e gli assegna una variabile chiamata valute
valute = database.database_valuta()

# Stampa le opzioni di conversione
print("Scegli l'opzione di conversione:")
print("1. Euro --> Yen")
print("2. Yen --> Euro")
print("3. Euro --> Cny")
print("4. Cny --> Euro")
print("5. Euro --> Sterlina")
print("6. Sterlina --> Euro")
print("7. Euro --> Rublo")
print("8. Rublo --> Euro")

# Chiedi all'utente quale valuta vuole convertire
numeroCambio = input("Inserisci che valuta vuoi convertire: ")

if numeroCambio.isdigit():  # Verifica se l'input è un numero
    numeroCambio = int(numeroCambio)
    if 1 <= numeroCambio <= 8:  # Verifica che l'input sia nel range, se no stampa un errore (rigo 27-28)
        print("Hai scelto l'opzione", numeroCambio)
    elif numeroCambio == 420:  # Piccolo Easter Egg
        print("seeeee")
    else:
        print("Scrivi un numero tra 1 e 8!", numeroCambio, "in questo caso non è valido")

        # Chiedi la quantità da convertire
    qnt = input("Inserisci la quantità di valuta da convertire: ")
    if qnt.isdigit():  # Verifica se l'input è un numero
        qnt = int(qnt)  # Imposta che la variabile 'qnt' sia un numero che possibilmente abbia la virgola

        # Controlla quale numero hai scelto ed esegue la conversione
        if numeroCambio == 1:
            print(qnt, "Euro in Yen sono:", qnt * valute["Yen"])
        elif numeroCambio == 2:
            print(qnt, "Yen in Euro sono:", qnt * valute["Yen"])
        elif numeroCambio == 3:
            print(qnt, "Euro in Cny sono:", qnt * valute["Cny"])
        elif numeroCambio == 4:
            print(qnt, "Cny in Euro sono:", qnt * valute["Cny"])
        elif numeroCambio == 5:
            print(qnt, "Euro in Sterline sono:", qnt * valute["Sterlina"])
        elif numeroCambio == 6:
            print(qnt, "Sterline in Euro sono:", qnt * valute["Sterlina"])
        elif numeroCambio == 7:
            print(qnt, "Euro in Rubli sono:", qnt * valute["Rublo"])
        elif numeroCambio == 8:
            print(qnt, "Rubli in Euro sono:", qnt * valute["Rublo"])
