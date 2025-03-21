class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_variable(self, name, value):
        self.symbols[name] = {'type': 'variable', 'value': value}

    def add_constant(self, name, value):
        self.symbols[name] = {'type': 'constant', 'value': value}

    def get_symbol(self, name):
        return self.symbols.get(name, None) 