#variabili globali e variabili locali
# ambito di visdibilità globale e locale

x = 15

def funzione_esempio():
    return x

print(funzione_esempio())

# in Python il codice e quindi anche le variabili, possono essere "salvati" in due ambienti diversi chiamati local scope e global scope, traducibili sostanzialmente come ambito di visibilità locale e globale

#Un ambito locale viene creato ogni volta che una funzione viene chiamata, e distrutto dopo che la funzione restituisce un valore con return.

#Per poter modificare il valore di una variabile globale dall'interno di una funzione, come abbiamo provato a fare con la nostra x, dobbiamo prima dichiarare alla funzione le nostre intenzioni mediante l'istruzione global. Modifichiamo l'esempio precedente:

# 1
x = 15

def funzione_esempio():
    global x
    x += 2
    return x


print(funzione_esempio())

# oppure es 1

x = 15

def funzione_esempio():
    y = x
    y += 2
    return y

print(funzione_esempio())

#3
def mia_funzione():
    val = 24
    return val

new_val = mia_funzione() + 6
print(new_val)

# quindi in sostanza sè devo richiamare  una variabile globale all'interno di una funzione per poterla modificare o semplicemente gestirla, ho utilizzo la keyword global per dichiararla all'interno della funzione oppure richiamo quella variabile inserendola all'interno di una nuova variabile oppure richiamre la funzione con all'iterno una nuova variabile e inserirla in una variabile per poi printarla