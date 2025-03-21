from evaluator import evaluate_expression

def assign_variable(name, expression, symbol_table):
    value = evaluate_expression(expression, symbol_table)
    symbol_table.add_variable(name, value)
    print(f"Asignación: {name} = {expression} => {value:.4f}") 