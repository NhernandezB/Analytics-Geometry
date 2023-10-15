import math

def calcular_distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def calcular_angulos_internos(coordenadas):
    # Asumimos que las coordenadas son una lista de tres puntos (x, y)
    if len(coordenadas) != 3:
        return "Se requieren exactamente tres puntos para formar un triángulo."

    # Calcula las longitudes de los lados del triángulo
    a = calcular_distancia(coordenadas[0], coordenadas[1])
    b = calcular_distancia(coordenadas[1], coordenadas[2])
    c = calcular_distancia(coordenadas[2], coordenadas[0])

    # Calcula los ángulos internos usando el teorema del coseno
    angulo_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angulo_B = math.degrees(math.acos((c**2 + a**2 - b**2) / (2 * c * a)))
    angulo_C = 180 - angulo_A - angulo_B

    return angulo_A, angulo_B, angulo_C

# Ejemplo de uso
coordenadas = [(-2, 1), (2, 1), (2, -3)]
angulos = calcular_angulos_internos(coordenadas)
print(f"Ángulo A: {angulos[0]} grados")
print(f"Ángulo B: {angulos[1]} grados")
print(f"Ángulo C: {angulos[2]} grados")