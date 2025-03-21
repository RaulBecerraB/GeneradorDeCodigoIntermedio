class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.next_id = 1

    def add_variable(self, name, value):
        if name in self.symbols and self.symbols[name]['type'] == 'constant':
            raise ValueError(f"No se puede modificar la constante '{name}'")
            
        self.symbols[name] = {
            'id': self.next_id,
            'type': 'variable', 
            'value': value
        }
        self.next_id += 1
        return self.symbols[name]

    def add_constant(self, name, value):
        if name in self.symbols:
            raise ValueError(f"El símbolo '{name}' ya está definido")
            
        self.symbols[name] = {
            'id': self.next_id,
            'type': 'constant', 
            'value': value
        }
        self.next_id += 1
        return self.symbols[name]

    def get_symbol(self, name):
        return self.symbols.get(name, None)
        
    def symbol_exists(self, name):
        return name in self.symbols
        
    def update_variable(self, name, value):
        if name not in self.symbols:
            raise ValueError(f"La variable '{name}' no está definida")
            
        if self.symbols[name]['type'] == 'constant':
            raise ValueError(f"No se puede modificar la constante '{name}'")
            
        self.symbols[name]['value'] = value
        return self.symbols[name] 