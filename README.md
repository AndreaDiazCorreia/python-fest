# Escribiendo Mejor Código Python: Una Guía Práctica

Este repositorio contiene ejemplos prácticos y explicaciones detalladas sobre cómo escribir código Python más elegante, eficiente y mantenible. Diseñado para programadores principiantes e intermedios, este material te guiará a través de los principios fundamentales y patrones avanzados que transformarán tu forma de programar en Python.

La guía está estructurada como un recorrido progresivo, desde conceptos básicos hasta técnicas más avanzadas, mostrando siempre ejemplos comparativos entre código "común" y código "pythónico".

## Contenido

El tutorial está dividido en cuatro secciones principales, cada una enfocada en un aspecto diferente de la programación en Python. Cada sección contiene ejemplos ejecutables que puedes probar por ti mismo para comprender mejor los conceptos.

### 1. El Poder de la Expresividad

Esta sección inicial muestra dos formas de resolver el mismo problema: una forma "principiante" y una forma "pythónica". La comparación ilustra cómo Python permite expresar ideas complejas de manera concisa y legible.

Ejemplo destacado:
- Transformación de una lista de números para obtener los cuadrados de los números pares
- Comparación entre enfoque imperativo tradicional (bucles y condicionales) vs. comprensión de listas

```python
# Enfoque "principiante"
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i] * numeros[i])
    i += 1
print(f"Resultado: {pares}")

# Enfoque "pythónico"
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n**2 for n in numeros if n % 2 == 0]
print(f"Resultado: {pares}")
```

**Por qué importa**: El código pythónico no solo es más corto, sino que comunica la intención de manera más clara, reduce la posibilidad de errores y suele ser más eficiente. La comprensión de listas expresa directamente "qué" queremos (los cuadrados de los números pares) en lugar de detallar "cómo" obtenerlos paso a paso.

### 2. Filosofía en Acción: El Zen de Python

Esta sección explora los principios del Zen de Python a través de ejemplos prácticos, mostrando cómo estos principios guían el diseño de código más limpio y mantenible.

> Para ver el Zen de Python completo, ejecuta `import this` en tu intérprete de Python.

Conceptos clave:

#### **Explícito es mejor que implícito**

Usa nombres descriptivos y type hints para comunicar claramente la intención de tu código:

```python
# ❌ Implícito - no sabemos qué hace
def procesar_datos(datos):
    return [x for x in datos if x]

# ✅ Explícito - propósito claro
def obtener_valores_no_vacios(valores: list) -> list:
    return [valor for valor in valores if valor]
```

#### **Simple es mejor que complejo**

Evita abstracciones innecesarias cuando una solución directa es suficiente:

```python
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
```

#### **EAFP vs LBYL**

El enfoque pythónico prefiere "Es más fácil pedir perdón que permiso" sobre "Mirar antes de saltar":

```python
diccionario = {"nombre": "Alice", "edad": 30}

# ❌ LBYL - Look Before You Leap
if 'email' in diccionario:
    email = diccionario['email']
else:
    email = 'sin_email@ejemplo.com'

# ✅ EAFP - Easier to Ask for Forgiveness than Permission
try:
    email = diccionario['email']
except KeyError:
    email = 'sin_email@ejemplo.com'

# ✅ Más pythónico aún
email = diccionario.get('email', 'sin_email@ejemplo.com')
```

#### **Legibilidad cuenta**

Balancear concisión y claridad es crucial para mantener el código comprensible:

```python
data = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]

# ❌ Poco legible - "clever" pero confuso
resultado_confuso = [y for x in data for y in x if y > 0]

# ✅ Mejor: Legible Y conciso
def obtener_positivos(matriz):
    return [elemento for sublista in matriz 
            for elemento in sublista 
            if elemento > 0]
```

### 3. Patrones que Transforman: Herramientas Pythónicas

Esta sección presenta patrones y construcciones específicas de Python que pueden transformar radicalmente la forma en que escribes código.

#### **Comprensiones: Declarativo vs. Imperativo**

Las comprensiones permiten expresar transformaciones de datos de forma declarativa (qué quieres) en lugar de imperativa (cómo obtenerlo):

```python
usuarios = [
    Usuario("Alice", True),
    Usuario("Bob", False),
    Usuario("Charlie", True)
]

# ❌ Imperativo - describes CÓMO
usuarios_activos_imp = []
for usuario in usuarios:
    if usuario.activo:
        usuarios_activos_imp.append(usuario.nombre.upper())

# ✅ Declarativo - describes QUÉ
usuarios_activos_dec = [u.nombre.upper() for u in usuarios if u.activo]
```

#### **Context Managers: Gestión automática de recursos**

Los context managers (`with`) garantizan la liberación adecuada de recursos, incluso si ocurren errores:

```python
# ❌ Manual - propenso a errores
archivo = open('datos.txt', 'r')
contenido = archivo.read()  # ¿Qué pasa si esto falla?
archivo.close()  # ¿Se ejecuta siempre?

# ✅ Automático - garantizado
with open('datos.txt', 'r') as archivo:
    contenido = archivo.read()
    # Cierre automático incluso si hay error
```

Puedes crear tus propios context managers con `@contextmanager` o implementando los métodos `__enter__` y `__exit__`.

#### **Estructuras de datos adecuadas**

Elegir la estructura de datos correcta puede mejorar significativamente el rendimiento y la legibilidad:

```python
# Sets para pruebas de membresía (O(1) vs O(n))
usuarios_premium_lista = ['alice', 'bob', 'charlie'] * 1000
usuarios_premium_set = {'alice', 'bob', 'charlie'}

# Mucho más rápido con sets
usuario_test = 'bob'
usuario_test in usuarios_premium_set  # O(1)

# Enumerate para índices
elementos = ['Python', 'es', 'genial']

# ✅ Pythónico
for i, elemento in enumerate(elementos):
    print(f"{i}: {elemento}")
```

#### **F-strings: Formateo moderno**

La evolución del formateo de strings en Python:

```python
nombre = "Ana"
edad = 28

# Antiguo %
mensaje_viejo = "Hola, %s! Tienes %d años" % (nombre, edad)

# .format()
mensaje_format = "Hola, {}! Tienes {} años".format(nombre, edad)

# f-strings (Python 3.6+)
mensaje_f = f"Hola, {nombre}! Tienes {edad} años"

# Auto-documentación (Python 3.8+)
print(f"{nombre=}, {edad=}")

# Con expresiones
print(f"{nombre} {'aprobó' if edad >= 18 else 'no aprobó'}")
```

### 4. El Horizonte: Técnicas Avanzadas

Esta sección final ofrece un vistazo a técnicas más avanzadas que se construyen sobre los fundamentos pythónicos.

#### **Decoradores: Modificar el comportamiento de funciones**

Los decoradores permiten extender o modificar el comportamiento de funciones sin cambiar su código interno:

```python
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
```

#### **Generadores: Manejo eficiente de memoria**

Los generadores producen valores bajo demanda, lo que permite trabajar con secuencias potencialmente infinitas usando memoria constante:

```python
def fibonacci(n):
    """Genera n números de Fibonacci"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Uso eficiente de memoria
for num in fibonacci(10):
    print(num, end=" ")
```

#### **Type Hints avanzados: Documentación ejecutable**

Los type hints avanzados permiten expresar tipos complejos y mejorar las herramientas de análisis estático:

```python
from typing import Union, Optional, List, Dict, TypeVar, Generic

# Tipos unión
def procesar_mixto(datos: List[Union[str, int]]) -> Optional[str]:
    if not datos:
        return None
    return str(datos[0])

# Tipos genéricos (Python 3.9+)
T = TypeVar('T')
class Stack(Generic[T]):
    def push(self, item: T) -> None: ...
    def pop(self) -> T: ...
```

#### **Pattern Matching: Estructura de control moderna (Python 3.10+)**

El pattern matching permite manejar estructuras de datos complejas de manera elegante:

```python
def procesar_datos(datos):
    match datos:
        case {"tipo": "usuario", "activo": True}:
            return "Usuario activo"
        case {"tipo": "admin"}:
            return "Administrador"
        case [x, y]:
            return f"Coordenadas: {x}, {y}"
        case _:
            return "Datos desconocidos"
```

## Cómo usar este repositorio

Cada archivo Python en este repositorio contiene ejemplos ejecutables que ilustran los conceptos discutidos. Para obtener el máximo beneficio:

1. Ejecuta cada archivo en orden secuencial:
   ```
   python 01_intro.py
   python 02_filosofia.py
   python 03_patrones.py
   python 04_avanzado.py
   ```

2. Experimenta modificando los ejemplos para ver cómo cambia el comportamiento.

3. Intenta aplicar estos principios a tu propio código, refactorizando proyectos existentes.

## Recursos adicionales

Para profundizar en estos conceptos, recomendamos:

- [PEP 8 - Guía de estilo para Python](https://peps.python.org/pep-0008/)
- [PEP 20 - El Zen de Python](https://peps.python.org/pep-0020/)
- [Python Cookbook](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/) de David Beazley y Brian K. Jones
- [Fluent Python](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) de Luciano Ramalho
- [Real Python](https://realpython.com/) - Tutoriales y artículos sobre Python

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ejemplos adicionales o mejoras para los existentes, no dudes en enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.