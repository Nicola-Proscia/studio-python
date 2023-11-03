#le standard library di python https://docs.python.org/3/library/index.html
#le funzioni vengono dette anche moduli
#esiston due modalità di importazione dei moduli

#1
import random                          #qui abbiamo importato la libreria random

for number in range(20):                #classico ciclo for per generare numeri da 0 a 20 con la sintassi range
    container = random.randint(1, 6)    #in questa riga abbiamo creato una variabile e gli abbiamo assegnato con "random" il richiamo della libreria e con ".randiat" la funzione
    print(container)
    
#2

from random import randint  #gli gli stiamo dicendo che dalla libreria random  e di prendere la funzione randint( una funzione della libreria)
    
for number in range (20):    
    container = randint(1, 6)      #ci basta solo richimare la funzione senza richiamare la libreria
    print(container)