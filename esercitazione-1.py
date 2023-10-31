#ciao 
age = 30
testo = "ciao"
testo + str(30) #il int viene trasformato in str per poter sommare le stringhe

#esercizio
#1

robot_name = "Chappie"
robot_age = 1

print("Ciao! Il mio nome è " + robot_name + " e ho " + str(robot_age) + " anno")

user_name = input("Tu come ti chiami? ")
print("Ciao " + user_name + "!")

user_age = int(input("Quanti anni hai? "))
age_difference = user_age - robot_age

print(str(user_age) + " anni!? Sono " + str(age_difference) + " più di me!")
print("A presto!")


