from math import sqrt   #sqrt radice quadrata

hello_message= """
benvenuti al programma calcolatrice!

di seguito un elenco delle varie funzioni disponibili:

- Per effettuare un Adddzione, seleziona 1;
- Per effettuare una Sottrazione, seleziona 2;
- Per effettuare una Moltiplicazione, seleziona 3;
- Per effettuare una Divisione, seleziona 4;
- Per effettuare un Calcolo Esponenziale , seleziona 5;
- Per effettuare una Radice Quadrata, seleziona 6;
- Per uscire dal programma puoi digitare ESC;
"""

while True:
    
    print(hello_message)
    
    action= input("inserisci un numero corrispodente all'operazione da effettuare:  ")
    
    if action == "1":
        print("\n Hai scelto: addizione\n")
        a = float(input("inserisci il primo numero: "))          
        b = float(input("inserisci il secondo numero: "))
        print(" Il risultato dell'Addizione è : ", str(a+b))
        
    elif action == "2":
        print("\n Hai scelto: sottrazione\n")
        a = float(input("inserisci il primo numero: "))
        b = float(input("inserisci il secondo numero: "))
        print(" Il risultato della Sottrazione è: ", str(a-b))
    
    elif action == "3":
        print("\n Hai scelto: moltiplicazione\n")
        a = float(input("inserisci il primo numero: "))
        b = float(input("inserisci il secondo numero: "))
        print(" Il risultato della moltipilcazione è: ", str(a*b))
    
    elif action == "4":
        print("\n Hai scelto: divisione\n")
        a = float(input("inserisci il primo numero: "))
        b = float(input("inserisci il secondo numero: "))
        print(" Il risultato della divisione​ è: ", str(a/b))      
        
    new_action = input("\n Vuoi effettuare un'altra operazione? (S/N) ")
    if new_action == "S" or new_action == "s":
        print("Perfetto ritorno al menu principale")
        continue
    elif new_action == "N" or new_action == "n":
        print("Arrivederci")
        break
    else:
        print("Scelta non valida")
        break
              


