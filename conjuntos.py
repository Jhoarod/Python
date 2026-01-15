group1 = {"alana", "samuel", "alejandro", "isabela"}
group2 = {"samuel", "alejandro", "carlos", "oscar"}
group3 = {"isabela"}
group4 = ("alejandra", "luis", "samuel")
group5 = dict( uno = 1, dos= 2 , tres= 3)
""""
 Usa : dentro de {}
 O usa dict() con =
"""
intersection = group1.intersection(group2) #Cual es la intersección entre el grupo1 y grupo2

print(intersection)

inside = group3.issubset(group1) #Los elementos del grupo3 se encuentran en el grupo1
print(inside)

print(*group4, sep=" y ") #se usa * para desempaquetar el conjunto de elementos

print(group5)