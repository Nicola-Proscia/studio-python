#ciclo while (finche è e resta true)

#ciclo while classico
counter = 0

while counter <= 10:
    print(counter)
    counter += 1
    
#ciclo while loop
    
while 33 == 33:
    print("ciao")  

#ciclo while con break( interropere una situazione di loop ) 

run = True
stop = 4000
counter = 0

while run == True:
    print(counter)
    counter += 1
    if counter >= stop:
        print("dai amico mio usciamo dal ciclo")
        break
    
    
#ciclo while con continue (salta una parte di codice), quindi in questo caso salta l'ultimo print(counter) per eseguire print("Sto saltando " + str(skip))
    

skip = 5
counter = 0

while counter < 10:
    counter += 1
    if counter == skip:
        print("Sto saltando " + str(skip))
        continue
    print(counter)
    
    
