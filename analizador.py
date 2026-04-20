import re

def limpiar_texto(texto):
    return re.findall(r'\b\w+\b', texto.lower())

def contar_palabras(texto):
    palabras = limpiar_texto(texto)
    return len(palabras)

def contar_oraciones(texto):
    return len(re.findall(r'[.!?]+', texto))

def palabra_mas_frecuente(texto):
    palabras = limpiar_texto(texto)
    frecuencia = {}
    for p in palabras:
        frecuencia[p] = frecuencia.get(p, 0) + 1
    return max(frecuencia, key=frecuencia.get)

def palabras_unicas(texto):
    return set(limpiar_texto(texto))

def longitud_promedio_palabras(texto):
    palabras = limpiar_texto(texto)
    if not palabras:
        return 0
    total = sum(len(p) for p in palabras)
    return total / len(palabras)

def buscar_palabra(texto, palabra):
    palabras = limpiar_texto(texto)
    palabra = palabra.lower()
    return palabras.count(palabra)

def reemplazar_palabra(texto, vieja, nueva):
    return re.sub(rf'\b{vieja}\b', nueva, texto)


texto_ejemplo = """
Python es un lenguaje de programación muy popular. Python es fácil de aprender.
Muchos programadores usan Python para ciencia de datos y para desarrollo web.
Python tiene una gran comunidad. La comunidad de Python es muy activa y amigable.
¿Te gusta programar? ¡Python es una excelente opción para empezar!
"""

print("=== ANALIZADOR DE TEXTO ===")
print(f"Total de palabras: {contar_palabras(texto_ejemplo)}")
print(f"Total de oraciones: {contar_oraciones(texto_ejemplo)}")
print(f"Palabra más frecuente: {palabra_mas_frecuente(texto_ejemplo)}")
print(f"Palabras únicas: {len(palabras_unicas(texto_ejemplo))}")
print(f"Longitud promedio: {longitud_promedio_palabras(texto_ejemplo):.1f}")
print(f"Veces que aparece 'Python': {buscar_palabra(texto_ejemplo, 'Python')}")

nuevo = reemplazar_palabra(texto_ejemplo, "Python", "Java")
print(f"\nTexto modificado (primeras 100 letras):\n{nuevo[:100]}...")
