#gestione degli errori
#try = prova, (tipo IF)
#except = eccetto,eccezione (tipo ELSE)
#finally = sempre

def moltipicazione():
    try:                                                  #esegui il docice , prova il codice
        a = int(input("inserisci un numero "))
        b = int(input("inserisci un altro numero "))
        c = a*b
        print(c)
    except ValueError:                                    #eccetto che si verifiche questo errore,non mi presentare 
        print("devi inserire un numero")                  #il tipo di errore ma lasciamo il messaggio relativo all'errore
    finally:
        print("chiudo l'applicazione")                     #messaggio che in ogni caso si manifesta a prescindere
                                                            #se la funzione dia un risulato o un errore
    
        
moltipicazione()            


#come buon usanza è meglio non eseguire il codice su tutta la funzione ma solo sulle funzioni che ci servono

#inoltre possiamo inoltre utilizzare nelle asezione except e il ValueError , as e: per poterlo richiamare e visualizzare il reale errore gestito da python
