"""
Equipos de futbol 
del mundo
"""

españa = ["Real Madrid", "Barcelona", "Atletico de Madrid", "Villareal"]
inglaterra = ["Chelsea", "Arsenal", "Wolf", "Manchester United", "Manchester City"]
francia = ["Monaco", "Psg", "Rens", "Olympique Marsella"]
italia = ["Juventus", "Napoles", "Inter", "Ac Milan", "Fiorentina"]
alemania = list("Bayer munich") #Con la funcion list me deletrea la palabra letra por letra, y solo recibe un argumento.
pais = str(input("ingresa un pais:"))
if any ([pais]):
        print("Equipos de futbol")
else :
     print("No existen")


print(alemania)