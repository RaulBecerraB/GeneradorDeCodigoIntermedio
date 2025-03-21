from symbol_table import SymbolTable
from evaluator import evaluate_expression
from assignment import assign_variable

def main():
    symbol_table = SymbolTable()
    print("=== Mini Compilador ===")
    
    # Definir constantes
    symbol_table.add_constant("PI", 3.1416)
    print("Constante definida: PI = 3.1416")
    
    # Solicitar variables al usuario
    variables_default = ["radio"]
    print("\n--- Ingreso de variables ---")
    
    for var in variables_default:
        valor = float(input(f"Ingrese el valor de {var}: "))
        symbol_table.add_variable(var, valor)
        print(f"Variable definida: {var} = {valor}")
    
    # Permitir al usuario añadir más variables
    while True:
        nueva_var = input("\n¿Desea agregar otra variable? (nombre o 'no' para continuar): ")
        if nueva_var.lower() == 'no':
            break
            
        try:
            valor = float(input(f"Ingrese el valor de {nueva_var}: "))
            symbol_table.add_variable(nueva_var, valor)
            print(f"Variable definida: {nueva_var} = {valor}")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Definir expresiones a evaluar
    print("\n--- Evaluación de expresiones ---")
    expresiones = {
        "area": "PI * radio * radio",
        "diametro": "2 * radio",
        "perimetro": "2 * PI * radio"
    }
    
    resultados = {}
    
    # Evaluar expresiones
    for nombre, expr in expresiones.items():
        try:
            valor = evaluate_expression(expr, symbol_table)
            assign_variable(nombre, expr, symbol_table)
            resultados[nombre] = valor
            print("")  # Línea en blanco para separar evaluaciones
        except Exception as e:
            print(f"Error al evaluar {nombre}: {e}")
    
    # Mostrar resultados
    print("\n--- Resultados ---")
    for nombre, valor in resultados.items():
        print(f"{nombre} = {valor:.4f}")
    
    # Opción para evaluar expresiones personalizadas
    print("\n--- Evaluación de expresiones personalizadas ---")
    while True:
        expr_personalizada = input("Ingrese una expresión a evaluar (o 'salir' para terminar): ")
        if expr_personalizada.lower() == 'salir':
            break
        
        try:
            resultado = evaluate_expression(expr_personalizada, symbol_table)
            print(f"Resultado: {resultado:.4f}")
            
            nombre_var = input("¿Desea guardar este resultado? Ingrese nombre de variable (o Enter para no guardar): ")
            if nombre_var:
                assign_variable(nombre_var, expr_personalizada, symbol_table)
        except Exception as e:
            print(f"Error al evaluar la expresión: {e}")
    
    # Mostrar la tabla de símbolos
    print("\n--- Tabla de símbolos final ---")
    print(f"{'ID':<4} {'Nombre':<12} {'Tipo':<10} {'Valor':<10}")
    print("-" * 40)
    for name, info in sorted(symbol_table.symbols.items(), key=lambda x: x[1]['id']):
        print(f"{info['id']:<4} {name:<12} {info['type']:<10} {info['value']:<10}")

if __name__ == "__main__":
    main() 