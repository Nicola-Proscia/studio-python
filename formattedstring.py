#è possbilile con la funzione FORMATTED STRING concatenare valori tra int string e float utilizzando il comando "f"

name="Nicola"
numero=1

frase = f"{numero} {name}"
print(frase)

#il metrodo delle stringhe

#abbiamo due tipoligie di metodi che possiamo concatenare OVVERO

# - startswitch() : se la parola da controllare inizia con la parola che ci si passa come argomento restituisce un valore booleano True o false
# - endswith() : se la parola da controllare termina con la parola che ci si passa come argomento restituisce un valore booleano True o false

nome="Nicola"
print(nome.startswith("N"))

surnmame="Proscia"
print(surnmame.endswith("a"))

# esisono altri metodi isalnum() isalpha() isdecimal() isspace()
# - isalnum() : verifica se una parola è composta solo da lettere e numeri restituisce un valore booleano True o False
# - isalpha() : verifica se una parola XVI composta solo da lettere restituisce un valore booleano True o False
# - isdecimal() : verifica se una parola XVI composta solo da numeri restituisce un valore booleano True o False
# - isspace() : verifica se una parola XVI composta solo da spazi restituisce un valore booleano True o False

spam = "asd123"
eggs = "999"
bacon = "   "
monty = "poker "

print(spam.isalnum())

print(spam.isalpha())

print(eggs.isdecimal())

print(eggs.isalnum())

print(monty.isspace())

print(bacon.isspace())

# i metodi upper() lower() 
# - upper() : converte una parola XVI in maiuscolo
# - lower() : converte una parola in minuscolo

name = "Alice"

print(name.lower()) 
print(name.upper())

# N.B. per cambiare il valore e sovrascriverlo dobbiamo dare una nuova variabile

name = name.upper()
print(name)

#metodi split() e join()

# - split() : separa una parola in una lista di parole
# - join() : unisce una lista di parole in una parola

words = "The quick brown fox jumps over the lazy dog"
print(words.split())

print("-".join(words.split()))

citazione = "Nel mezzo del cammin di nostra vita..."

print (citazione.split(" "))

['Nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita...']  # <- restituisce una lista


#--------------------------------

#La funzione len()
# La funzione integrata di Python len() ci permette di ottenere la lunghezza di una lista o una stringa, e quindi rispettivamente il numero di elementi o di caratteri presenti in queste:

my_str = "spam, eggs, bacon, spam"

my_list = ["spam", "spam", "spam"]

print(len(my_str))  # <- restituisce il numero di elementi

print(len(my_list))  # <- restituisce il numero di elementi

#cicli FOR
#POSSIAMO INOLTRE CONTROLLARE ALL'INTERNO DI STRINGHE QUALI LETTERE SONO PRESENTI NELLA STRINGA

parola = "niosaduybfoyfsydufvugfsasosbv"
match = "s"
counter = 0

for el in parola:
    if el == match:
        counter += 1
        
output = f"ho trovato all'interno {counter} lettere {match}"        
print(output)