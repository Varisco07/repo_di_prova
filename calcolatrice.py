while True:
    print("Benveuto nella nostra calcolatrice")
    print("Inserisci l'operazione che vuoi effettuare")
    scelta = int(input("1)sottrazione\n2)addizione\n0)exit"))
    if scelta == 0:
        break
    elif scelta == 1:
        n_1 = int(input("Inserisci il primo numero: "))
        n_2 = int(input("Inserisci il secondo numero: "))
        print(f"{n_1} - {n_2} = {n_1 - n_2}")
    elif scelta == 2:
        n_1 = int(input("Inserisci il primo numero: "))
        n_2 = int(input("Inserisci il secondo numero: "))
        print(f"{n_1} + {n_2} = {n_1 + n_2}")
    else: 
        print("Scelta non corretta!!")