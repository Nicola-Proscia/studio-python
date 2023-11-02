#i dizionari sono un tipo di dato sono simi alle liste ma a differenza di queste ad ogni lemento non è associato un indice ma è associata una chiave
#si rappresentano sempre come i set e si utilizzano le parentesi quadre
#all'interno delle parentesi quadre la sintassi viene gestita con la sequenza "chiave" : "valore"
#la chiave puo essere di qualsiasi tipo con anche il valore 
#all'interno di un dizionario per dividere una chiave/valore da un altra si usa la " , "

#un esempio di dizionario

my_dict = {"chiave" : "valore", "chiave2" : 12, 4.20 : "ciao"}

# se mandiamo in print una chiave ci restituira il valore associato
# inoltre possiamo aggiungere o modificare un valore semplicemente chimando la chiave e facendo un uguale in modo da sovrascrivere il valore

my_dict["chiave"] = 34   #cosi diciamo di prendere la chiave con nome chiave e di cambiare il suo 
print(my_dict)           #valore in 34

#possiamo inoltre aggiungere una nuova chiave/valore seguendo lo stesso procedimento della modifica

my_dict["nuova_chiave"] = 56  #questa chiave valore che prima non era presente ora verrà implementata  
print(my_dict) 

# per verificare sè una chiave  presente si possono usare gli operatore "in " e "not in " che resitutisce un valore booleano
#N.B. sè verifichiamo un valore ci restituirà sempre false perchè la ricerca con questi operatore è solo per le chiavi

search = "nuova_chiave" in my_dict
print(search)

#si possono cancellare anche elementi come ad esempio

del my_dict["nuova_chiave"]
print(my_dict)



#I METODI DIZIONARI

#Esistono metodi per poter visualizzare all'interno di un dizionario:
# - keys() : restitutte le chiavi 
# - values() : restitutte i valori
# - items() : restitutte le chiavi e i valori

my_dict.keys()
my_dict.values()
my_dict.items()

#lanciando questi comandi noteremo che i risultati verranno restituiti non come semplici liste ma come tuple e che verrà restituito sotto forma di oggetto di tYPE :
# dict_keys, dict_values, dict_items  

# Si possono fare dei cicli per visualizzare i valori di una chiave le chiavi o le coppie chiave-valore

for chiave in my_dict.keys():
    print(chiave)

for valore in my_dict.values():
    print(valore)

for chiave, valore in my_dict.items():
    print(chiave, valore)

#mettiamo il caso che vogliamo cercare un valore che non è presente all'interno del dizionario
# di solito faremmo 
if "birra" in my_dict:
    print("ci sono")
else:
    print("non ci sono")
    
#python ci viene in contro semplificando il tutto con il metodo get()    

my_dict.get("birra", "chiave non trovata") #visto che non troverà la birra nel dizionario ci setituire la risposta                                  

my_dict.get("chiave", "chiave non trovata") #visto che qui troverà la stringa chiave allora ci resituira il suo valore in output

#possiamo trovarci ad un punto del codice ed avere bisogno di aggingere una nuova chiave valore 
#tutto ciò si può fare con la funzion setdefault()

my_dict.setdefault("chiave", "valore")
