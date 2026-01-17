"""
Equipos de fútbol del mundo
"""

equipos = [
    "Real Madrid", "Barcelona", "Atletico de Madrid", "Villarreal",
    "Chelsea", "Arsenal", "Wolves", "Manchester United", "Manchester City",
    "Monaco", "PSG", "Rennes", "Olympique Marsella",
    "Juventus", "Napoles", "Inter", "AC Milan", "Fiorentina", "Bayer munich"
]

equipo = str(input("Ingresa un equipo de fútbol: "))

if equipo in equipos:
    print("El equipo existe en la lista")
else:
    print("El equipo no existe en la lista")
