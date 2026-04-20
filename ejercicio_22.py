def usar_la_fuerza(mochila, objetos_sacados=0):
    # CASO BASE 1: Si la mochila está vacía, no encontramos el sable
    if len(mochila) == 0:
        print("La mochila está vacía y no se encontró el sable de luz.")
        return False, objetos_sacados

    # Sacamos el objeto que está arriba (el último del vector)
    objeto = mochila.pop()
    objetos_sacados += 1
    
    # CASO BASE 2: Si el objeto es el sable de luz
    if objeto == "sable de luz":
        print(f"¡Fuerza encontrada! Se encontró el sable de luz.")
        print(f"Se tuvieron que sacar {objetos_sacados} objetos para encontrarlo.")
        return True, objetos_sacados
    
    # LLAMADA RECURSIVA: Si no es el sable, volvemos a llamar a la función
    # pero ahora la mochila tiene un objeto menos
    return usar_la_fuerza(mochila, objetos_sacados)

# --- Probando la función ---
# Creamos el vector (mochila) con varios objetos
mi_mochila = ["comida", "holocron", "sable de luz", "capa", "herramientas"]

print("Buscando el sable de luz en la mochila...")
encontrado, cantidad = usar_la_fuerza(mi_mochila)

if not encontrado:
    print("El Jedi tendrá que usar otra estrategia.")