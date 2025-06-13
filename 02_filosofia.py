# ============================================
# 2. FILOSOFÍA EN ACCIÓN (10 minutos)
# ============================================
print("=== FILOSOFÍA EN ACCIÓN ===")
print("El Zen de Python no es poesía, es tu GPS para código")
print()

# --- Ejemplo 1: Explícito es mejor que implícito ---
print("--- 1. Explícito es mejor que implícito ---")

# ❌ Implícito - no sabemos qué hace
def procesar_datos(datos):
    return [x for x in datos if x]

# ✅ Explícito - propósito claro
def obtener_valores_no_vacios(valores: list) -> list:
    return [valor for valor in valores if valor]

# Demo
datos_test = ["Alice", "", "Bob", None, "Charlie", ""]
print(f"Datos: {datos_test}")
print(f"Implícito: {procesar_datos(datos_test)}")
print(f"Explícito: {obtener_valores_no_vacios(datos_test)}")
print("Names matter! Type hints comunican intención.")
print()

# --- Ejemplo 2: Simple es mejor que complejo ---
print("--- 2. Simple es mejor que complejo ---")

# ❌ Complejo - sobreingeniería
class StringProcessor:
    def __init__(self):
        self.operations = []
    
    def add_operation(self, op):
        self.operations.append(op)
    
    def process(self, text):
        for op in self.operations:
            text = op(text)
        return text

# ✅ Simple - soluciona el problema real
def limpiar_texto(texto: str) -> str:
    return texto.strip().lower().replace(" ", "_")

# Demo
texto_ejemplo = "  Hola Mundo Python  "
print(f"Texto original: '{texto_ejemplo}'")

# Versión compleja
processor = StringProcessor()
processor.add_operation(lambda x: x.strip())
processor.add_operation(lambda x: x.lower())
processor.add_operation(lambda x: x.replace(" ", "_"))
resultado_complejo = processor.process(texto_ejemplo)

# Versión simple
resultado_simple = limpiar_texto(texto_ejemplo)

print(f"Complejo: '{resultado_complejo}'")
print(f"Simple: '{resultado_simple}'")
print("Pregunta clave: ¿Realmente necesito esta abstracción?")
print()

# --- Ejemplo 3: EAFP vs LBYL ---
print("--- 3. EAFP vs LBYL ---")

diccionario = {"nombre": "Alice", "edad": 30}

# ❌ LBYL - Look Before You Leap
print("LBYL (Look Before You Leap):")
if 'email' in diccionario:
    email = diccionario['email']
else:
    email = 'sin_email@ejemplo.com'
print(f"Email LBYL: {email}")

# ✅ EAFP - Easier to Ask for Forgiveness than Permission
print("EAFP (Easier to Ask for Forgiveness than Permission):")
try:
    email = diccionario['email']
except KeyError:
    email = 'sin_email@ejemplo.com'
print(f"Email EAFP: {email}")

# ✅ Más pythonico aún
email = diccionario.get('email', 'sin_email@ejemplo.com')
print(f"Email pythonico: {email}")
print("EAFP es más rápido cuando la clave existe (caso común)")
print()

# --- Ejemplo 4: Legibilidad cuenta ---
print("--- 4. Legibilidad cuenta ---")

# Data de ejemplo
data = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]

# ❌ Poco legible - "clever" pero confuso
resultado_confuso = [y for x in data for y in x if y > 0]
print(f"Confuso: {resultado_confuso}")

# ✅ Legible - pasos claros
elementos_positivos = []
for sublista in data:
    for elemento in sublista:
        if elemento > 0:
            elementos_positivos.append(elemento)
print(f"Legible: {elementos_positivos}")

# ✅ Mejor: Legible Y conciso
def obtener_positivos(matriz):
    return [elemento for sublista in matriz 
            for elemento in sublista 
            if elemento > 0]

resultado_mejor = obtener_positivos(data)
print(f"Mejor: {resultado_mejor}")
print("Balance entre concisión y claridad")
print()

# NOTAS PARA LA PRESENTACIÓN:
# - Ejecutar cada ejemplo por separado
# - Hacer pausas entre ejemplos
# - Enfatizar los principios del Zen
# - Mostrar que cada ejemplo ilustra un principio específico
# - Preguntar: "¿Han visto código así?" después de los ejemplos malos