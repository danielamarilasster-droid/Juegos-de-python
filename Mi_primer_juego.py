import random

print("====================================")
print("  ¡BIENVENIDO AL JUEGO, jugador!   ")
print("====================================")

# Elige tu arma
tu_opcion = input("Elige (piedra, papel o tijera): ").lower()

# La computadora elige al azar
opciones = ["piedra", "papel", "tijera"]
computadora = random.choice(opciones)

print(f"\nTú elegiste: {tu_opcion}")
print(f"La computadora eligió: {computadora}")
print("------------------------------------")

# Aquí el código revisa quién gana
if tu_opcion == computadora:
    print("¡Es un empate! 🤝")
elif tu_opcion == "piedra" and computadora == "tijera":
    print("¡Ganaste, jugador! La piedra rompe la tijera. 🏆")
elif tu_opcion == "papel" and computadora == "piedra":
    print("¡Ganaste, jugador! El papel envuelve la piedra. 🏆")
elif tu_opcion == "tijera" and computadora == "papel":
    print("¡Ganaste, Daniel! La tijera corta el papel. 🏆")
else:
    print("¡Ganó la computadora! ¡Inténtalo otra vez! 🤖")
