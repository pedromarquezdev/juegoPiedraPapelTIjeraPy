#Juego piedra papel o tijera en python.
#
import random

palabrasDelJuego = ["Piedra", "Papel","Tijera"]

def juego():
    print("Elija que tirar: ")
    for i in range(len(palabrasDelJuego)):
        print(f"La opción {i+1} es: {palabrasDelJuego[i]}")
            
    while True:
        opcionElegida = int((input("Ingrese el número de su elección:")).strip())

        if 1 <= opcionElegida <= 3:
            print(f"La opción elegida fue: {palabrasDelJuego[opcionElegida -1]}.")
            palabraElegida = palabrasDelJuego[opcionElegida -1].lower()
            break
        else:
            print("Debe elegir una opción correcta 1,2 o 3.")
    eleccionMaquina = random.choice(palabrasDelJuego).lower()
    if eleccionMaquina == palabraElegida:
        print(f"Han empatado, has elegido {palabraElegida} y el oponente eligió {eleccionMaquina}")
    elif eleccionMaquina == "piedra" and palabraElegida == "papel":
        print(f"El oponente sacó: {eleccionMaquina} y tu {palabraElegida}")
        print("Has ganado")
    elif eleccionMaquina == "papel" and palabraElegida == "tijera":
        print(f"El oponente sacó: {eleccionMaquina} y tu {palabraElegida}")
        print("Has ganado")
    elif eleccionMaquina == "tijera" and palabraElegida == "piedra":
        print(f"El oponente sacó: {eleccionMaquina} y tu {palabraElegida}")
        print("Has ganado")
    elif eleccionMaquina == "papel" and palabraElegida == "piedra":
        print(f"El oponente sacó: {eleccionMaquina} y tu {palabraElegida}")
        print("Has perdido")
    elif eleccionMaquina == "tijera" and palabraElegida == "papel":
        print(f"El oponente sacó: {eleccionMaquina} y tu {palabraElegida}")
        print("Has perdido")
    elif eleccionMaquina == "piedra" and palabraElegida == "tijera":
        print(f"El oponente sacó: {eleccionMaquina} y tu {palabraElegida}")
        print("Has perdido")
    

juego()
