# Pongo float porque la temperatura y el viento pueden tener decimales, y el input devuelve un string, entonces lo convierto a float para poder hacer las comparaciones numéricas.
temperatura = float(input("Introduce la temperatura actual en °C: ")) # Solicitar al operario que ingrese la temperatura actual
viento = float(input("Introduce la velocidad del viento en km/h: ")) # Solicitar al usuario que ingrese la velocidad del viento

print("\n--- ESTADO DEL SISTEMA ---")

# CODIGOS DE COLOR

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
NARANJA_REAL = "\033[38;5;208m"

# Lógica de Alertas para Temperatura
if temperatura >= 42:
    print(f"{ROJO} ALERTA ROJA: Riesgo extremo por calor - Riesgo para la salud muy alto.")
elif temperatura >= 39:
    print(f"{NARANJA_REAL}ALERTA NARANJA: Riesgo importante por calor - Se recomienda no salir en horas centrales del día.")
elif temperatura >= 36:
    print(f"{AMARILLO}ALERTA AMARILLA: Riesgo por calor - Se recomienda no realizar actividades al aire libre.")
else:
    print(f"{VERDE}Temperatura: Nivel Verde (Sin riesgo).")

# Lógica de Alertas para Viento
if viento >= 110:
    print(f"{ROJO}ALERTA ROJA: Viento extremo - Peligro de caída de objetos y daños estructurales.")
elif viento >= 90:
    print(f"{NARANJA_REAL}ALERTA NARANJA: Cierre preventivo de parques.")
elif viento >= 70:
    print(f"{AMARILLO}ALERTA AMARILLA: Balizas en zonas infantiles y de mayores")
else:
    print(f"{VERDE}Viento: Nivel Verde (Sin riesgo).")



