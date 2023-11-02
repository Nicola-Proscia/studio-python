parola = "niosaduybfoyfsydufvugfsasosbv"
match = "s"
counter = 0

for el in parola:
    if el == match:
        counter += 1
        
output = f"ho trovato all'interno {counter} lettere {match}"        
print(output)