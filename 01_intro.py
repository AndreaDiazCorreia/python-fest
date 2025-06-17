

# Código A - "Principiante"
print("Código A:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i] * numeros[i])
    i += 1
print(f"Resultado: {pares}")
print()

# Código B - "Pythonico"
print("Código B:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n**2 for n in numeros if n % 2 == 0]
print(f"Resultado: {pares}")
print()

print("¿Cuál preferirían encontrar en un proyecto real?")
print("No es magia... es filosofía.")
print()

# NOTAS PARA LA PRESENTACIÓN:
# - Ejecutar Código A primero, hacer pausa
# - Preguntar: "¿Qué hace este código?"
# - Ejecutar Código B, hacer pausa dramática
# - Enfatizar: "Mismo resultado, diferente filosofía"
# - Transición: "En 30 minutos van a entender el por qué"