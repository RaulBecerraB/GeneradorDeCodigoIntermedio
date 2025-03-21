def evaluate_expression(expression, symbol_table):
    for var in symbol_table.symbols:
        expression = expression.replace(var, str(symbol_table.symbols[var]['value']))
    return eval(expression) 