#le liste sono insiemi di valori che possono essere di vario tipo e si creano semplicemente dando il nome alla variabile seguito dal simbolo di assegnazione e poi i volori inseriti tra parentesi quadre

my_list =[23.4, "ciao", 5, "sono io"]

#ogni elemento ha un indice che parte da 0 per il primo elemento 
#con il -1 invece si accede all'ultimo elemento della lista (questo solo sè vogliamo ragionare al contrario)

#per richiamare un elemento usiamo
my_list[1]
my_list[-1]

new_list = [6, 7, "ciaone", my_list]

#si possono inoltre accorpare più liste tra di loro semplicemente inserendo all'interno della lista il nome della lista che vogliamo inserire

# se vogliamo richiamare in elemento specifico all'interno di una lista che si trova in una lista faremo cosi

new_list [1][2]  #il primo indice rappresenta la lista e il secondo indice rappresenta l'elemento della lista my_list


# list slicing (affettare)
#con questa moldalià possiamo prendere una parte di elemti all'interno di una lista facendo in questo modo
#data una lista prendimi tutti gli elementi dalla posizione 4 a 10
primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

primi[4:10]  #lanciando questo comando notremo che lui prende si i valori partendo da indice 4 ma si fermerà a indice 9

#sè invece questo comando lo associamo ad una variabile 
fetta = primi[4:10] #vedremo che prenderà anche l'elemento in posizione 10

#possiamo inoltre prendere degli elementi dando con inizio un indice senza dichiarare il range di fine in questo modo
primi[4:]

# possiamo ragionare al contrario dando una fine dell'indice e non un inizio(anche sè logicamente lui partirà sempre da indice 0)
primi[:5] #cosi facendo stiamo dicendo "prendi tutti gli elementi da indice 0 a indice 4 escluso 5"


#liste e Cicli for

primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

#possiamo far cliclare e controllare sè un valore dato in input si trovi all'interno della lista

match = 11  #valore in input

for el in primi:      #creamo il ciclo for (el = variabile ) in primi (lista)
    if el == match:   #se il valore in input è uguale a quello che ci si trova all'interno della lista
        print("trovato")
    else:
        print("non trovato")    
        
#i metodi delle liste

# per richiamare un metodo si utilizza la sintassi

# nomevaribile.nomemetodo(parametri)
#    per esempio    

spesa =["pane", "latte", "carne"]

spesa.append("uova")  #aggiunge un elemento alla fine della lista con APPEND

spesa2 = ["pane", "insalata", "lievito", "uova"] 

spesa.extend(spesa2)  #aggiunge una lista alla fine della lista con EXTEND

alfabeto = ["a", "b", "c"]

alfabeto.sort()  #ordina la lista con SORT

numeri = [4, 10, 3, 9, 5] 

numeri.sort()  #ordina la lista con SORT

numeri.reverse()  #inverte la lista   

#possiamo trovare l'indice dell'elemento all'interno della lista con INDEX

numeri = [4, 10, 3, 9, 5] 

numeri.index(9) #prendi l'indice dell'elemento 9

# -------------------------------------

#possiamo sostituire e rimuovere elementi all'interno della lista indicando solo l'indice

numeri = [4, 10, 3, 9, 5] 

numeri[1] = 7  #sostituisce l'elemento alla posizione 1 con 7

del spesa[0]  #rimuove l'elemento alla posizione 0

# -------------------------------------

new_list = [True, None, "poker", 4.20, 1945]

new_list.pop()  #rimuove l'ultimo elemento della lista

[True, None, 'poker', 4.2]

new_list.remove(None)  #rimuove l'elemento None

[True, 'poker', 4.2]