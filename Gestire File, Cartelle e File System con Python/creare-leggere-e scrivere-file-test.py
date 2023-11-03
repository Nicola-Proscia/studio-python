#write e append

# esempio di write
contenuto = "oggi è una bellissima giornata"     #diamo ad una variabile il contenuto di tipo testo
file1 = open("test.txt", "w")                      #diamo ad una variabile il nome di un file e con la funzione open di aprirlo
                                                 #oppure di crearlo qualore non esistesse
file1.write(contenuto)  
                        #richiamiamo la variabile con al funzione write per richiamare il testo con la sua variabile di riferimento
file1.close()             #con il comando close chiudiamo il file



#APPEND 
nuova_stringa = "\npython è una bomba!"   #per aggiungere testo ad un file esistente bisogna usare la funzione append
                      
file1 = open("test.txt", "a")            #la procedura si differenzia dall'inserimento di"a" in questa riga di codice

file1.write(nuova_stringa)   
file1.close()    

#read (leggera)  

var_lettura =open("test.txt", "r").read()   #con read per lettura semplice
print(var_lettura)

var_lettura =open("test.txt", "r").readlines()   #con readlines per leggere riga per riga 
print(var_lettura)

import os    #controllare percorso corrente
os.getcwd