# funzioni in python  , le funzioni possono essere create e richiamate ogni volta che vogliamo scrivendo solamente il nome della funzione

def addizione(a, b):
    print("Questa è la funzione addizione.")
    print("Fornisce la somma di due numeri passati come parametri.")
    risultato = a + b
    print("Il risultato dell'addizione è " + str(risultato))
    
addizione(10, 2)   #N.B l'indentazione è importante
    





def ex_fun_calc(a, b):
    addiction = a + b
    return addiction

somma = ex_fun_calc (2, 2) 
print (somma)


