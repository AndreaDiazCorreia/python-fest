# ============================================
# 3. PATRONES QUE TRANSFORMAN (12 minutos)
# ============================================
print("=== PATRONES QUE TRANSFORMAN ===")
print()

# --- Comprehensions: Declarativo vs Imperativo ---
print("--- Comprehensions: Declarativo vs Imperativo ---")

class Usuario:
    def __init__(self, nombre, activo):
        self.nombre = nombre
        self.activo = activo

usuarios = [
    Usuario("Alice", True),
    Usuario("Bob", False),
    Usuario("Charlie", True),
    Usuario("Diana", False),
    Usuario("Eve", True)
]

# ❌ Imperativo - describes CÓMO
print("Imperativo (CÓMO):")
usuarios_activos_imp = []
for usuario in usuarios:
    if usuario.activo:
        usuarios_activos_imp.append(usuario.nombre.upper())
print(f"Resultado: {usuarios_activos_imp}")

# ✅ Declarativo - describes QUÉ
print("Declarativo (QUÉ):")
usuarios_activos_dec = [u.nombre.upper() for u in usuarios if u.activo]
print(f"Resultado: {usuarios_activos_dec}")
print("Comprensiones = expresiones, no statements")
print("Menos propenso a errores, más rápido")
print()

# --- Context Managers ---
print("--- Context Managers: Gestión automática ---")

# Simulamos manejo de archivo
print("❌ Manual - propenso a errores:")
print("archivo = open('datos.txt', 'r')")
print("contenido = archivo.read()  # ¿Qué pasa si esto falla?")
print("archivo.close()  # ¿Se ejecuta siempre?")
print()

print("✅ Automático - garantizado:")
print("with open('datos.txt', 'r') as archivo:")
print("    contenido = archivo.read()")
print("    # Cierre automático incluso si hay error")
print()

# Demo con context manager personalizado
from contextlib import contextmanager
import time

@contextmanager
def cronometro(nombre):
    print(f"⏱️  Iniciando {nombre}...")
    inicio = time.time()
    try:
        yield
    finally:
        fin = time.time()
        print(f"⏱️  {nombre} terminó en {fin - inicio:.3f} segundos")

# Uso del context manager
with cronometro("operación demo"):
    time.sleep(0.1)  # Simula trabajo
    resultado = sum(range(100000))
    print(f"Resultado: {resultado}")

print("Context managers = protocolo __enter__ y __exit__")
print()

# --- Estructuras de datos adecuadas ---
print("--- Estructuras de datos adecuadas ---")

# Sets para membresía
print("Sets para pruebas de membresía:")
usuarios_premium_lista = ['alice', 'bob', 'charlie'] * 1000  # Lista grande
usuarios_premium_set = {'alice', 'bob', 'charlie'}

usuario_test = 'bob'

# Demo de velocidad (conceptual)
print(f"❌ Lista O(n): buscar '{usuario_test}' en {len(usuarios_premium_lista)} elementos")
print(f"✅ Set O(1): buscar '{usuario_test}' - hash lookup instantáneo")
print(f"En set: {usuario_test in usuarios_premium_set}")
print()

# Enumerate para índices
print("Enumerate para índices:")
elementos = ['Python', 'es', 'genial']

print("❌ Anti-patrón:")
for i in range(len(elementos)):
    print(f"  {i}: {elementos[i]}")

print("✅ Pythonico:")
for i, elemento in enumerate(elementos):
    print(f"  {i}: {elemento}")
print()

# --- F-strings: Formateo moderno ---
print("--- F-strings: Formateo moderno ---")

nombre = "Ana"
edad = 28
puntuacion = 95.67

print("Evolución del formateo:")

# Antiguo %
mensaje_viejo = "Hola, %s! Tienes %d años y sacaste %.1f" % (nombre, edad, puntuacion)
print(f"% formatting: {mensaje_viejo}")

# .format()
mensaje_format = "Hola, {}! Tienes {} años y sacaste {:.1f}".format(nombre, edad, puntuacion)
print(f".format(): {mensaje_format}")

# f-strings
mensaje_f = f"Hola, {nombre}! Tienes {edad} años y sacaste {puntuacion:.1f}"
print(f"f-strings: {mensaje_f}")

# Bonus: auto-documentación
print(f"Auto-doc: {nombre=}, {edad=}")

# F-strings con expresiones
print(f"Con expresión: {nombre} {'aprobó' if puntuacion >= 70 else 'reprobó'}")
print("F-strings: más rápidas, más legibles, más poderosas")
print()

# NOTAS PARA LA PRESENTACIÓN:
# - Este es el bloque más largo, administrar tiempo
# - Ejecutar cada patrón por separado
# - Hacer demostraciones en vivo del cronómetro
# - Enfatizar la diferencia visual entre código imperativo vs declarativo
# - Mostrar la evolución del formateo de strings paso a paso