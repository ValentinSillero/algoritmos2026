def romano_a_decimal(numero_romano):
    # Diccionario con los valores de cada símbolo
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    
    decimal = 0
    # Recorremos la cadena de texto
    for i in range(len(numero_romano)):
        valor_actual = valores[numero_romano[i]]
        
        # Si el valor actual es menor al siguiente, se resta (ej: IV = 4)
        if i + 1 < len(numero_romano) and valor_actual < valores[numero_romano[i+1]]:
            decimal -= valor_actual
        else:
            decimal += valor_actual
            
    return decimal

# Ejemplo de uso:
romano = "XIV" # Debería ser 14
print(f"El número romano {romano} en decimal es: {romano_a_decimal(romano)}")