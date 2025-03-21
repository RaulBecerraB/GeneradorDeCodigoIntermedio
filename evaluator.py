def evaluate_expression(expression, symbol_table):
    # Guardar la expresión original para mostrarla después
    original_expression = expression
    
    # Reemplazar todas las variables y constantes con sus valores
    print(f"Evaluando: {expression}")
    print("Sustituciones:")
    
    for var in symbol_table.symbols:
        if var in expression:
            value = str(symbol_table.symbols[var]['value'])
            print(f"  {var} -> {value}")
            expression = expression.replace(var, value)
    
    # Mostrar la expresión después de las sustituciones
    print(f"Expresión con valores: {expression}")
    
    # Evaluar la expresión
    result = eval(expression)
    print(f"Resultado: {result}")
    
    return result 