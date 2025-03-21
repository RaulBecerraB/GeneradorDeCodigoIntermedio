from symbol_table import SymbolTable
from evaluator import evaluate_expression
from assignment import assign_variable

def main():
    symbol_table = SymbolTable()

    # Solicitar valores al usuario
    radio = float(input("Ingrese el valor del radio: "))
    symbol_table.add_variable("radio", radio)
    symbol_table.add_constant("PI", 3.1416)

    # Calcular área y diámetro
    area_expr = "PI * radio * radio"
    diametro_expr = "2 * radio"
    
    area = evaluate_expression(area_expr, symbol_table)
    diametro = evaluate_expression(diametro_expr, symbol_table)
    
    symbol_table.add_variable("area", area)
    symbol_table.add_variable("diametro", diametro)
    
    print(f"Área del círculo: {area:.2f}")
    print(f"Diámetro del círculo: {diametro:.2f}")
    
    # Mostrar la tabla de símbolos
    print("\nTabla de símbolos actual:")
    for name, info in symbol_table.symbols.items():
        print(f"{name}: {info}")

if __name__ == "__main__":
    main() 