import Type
import json

class Attack:
    # Clase principal de ataques de Pokémon.

    def __init__(self, Type, dmg, accuracy, name, descr):
        self.Type = Type
        self.dmg = dmg
        self.accuracy = accuracy
        self.name = name
        self.descr = descr
    
    def loadJSON(self, name, j):
        pass