# ============================================
# 4. EL HORIZONTE (3 minutos)
# ============================================
print("=== EL HORIZONTE ===")
print("Estos fundamentos te abren la puerta a técnicas avanzadas:")
print()

# --- Decoradores ---
print("--- Decoradores ---")
import time
import functools

def timer(func):
    """Mide tiempo de ejecución"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️  {func.__name__} tardó {fin - inicio:.3f}s")
        return resultado
    return wrapper

@timer
def operacion_ejemplo():
    return sum(range(100000))

resultado = operacion_ejemplo()
print(f"Resultado: {resultado}")
print("Decoradores = funciones que modifican funciones")
print()

# --- Generadores ---
print("--- Generadores ---")
def fibonacci(n):
    """Genera n números de Fibonacci"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Primeros 10 números de Fibonacci:")
for num in fibonacci(10):
    print(num, end=" ")
print()
print("Generadores = memoria eficiente para grandes datasets")
print()

# --- Type Hints avanzados ---
print("--- Type Hints avanzados ---")
from typing import Union, Optional, List

def procesar_mixto(datos: List[Union[str, int]]) -> Optional[str]:
    """Procesa lista mixta de strings e ints"""
    if not datos:
        return None
    return str(datos[0])

resultado_mixed = procesar_mixto([42, "Python", 3.14])
print(f"Procesamiento mixto: {resultado_mixed}")
print("Type hints = documentación ejecutable")
print()

# --- Pattern Matching (Python 3.10+) ---
print("--- Pattern Matching (Python 3.10+) ---")
print("# Ejemplo conceptual - no ejecutable en todas las versiones")
print("""
def procesar_datos(datos):
    match datos:
        case {"tipo": "usuario", "activo": True}:
            return "Usuario activo"
        case {"tipo": "admin"}:
            return "Administrador"
        case _:
            return "Datos desconocidos"
""")
print("Pattern matching = poderoso para estructuras complejas")
print()

print("🚀 No necesitan dominar todo esto ahora.")
print("Estos fundamentos pythonicos son su base.")
print("Cuando los dominen, estas técnicas tendrán sentido naturalmente.")

# NOTAS PARA LA PRESENTACIÓN:
# - Este bloque debe ser rápido, es un "teaser"
# - Solo mostrar brevemente cada concepto
# - No profundizar, solo generar curiosidad
# - Enfatizar que son extensiones naturales de los fundamentos
# - Pattern matching mostrar solo como código comentado