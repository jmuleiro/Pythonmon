import json

# Clase de tipos de Pokémon o Ataques.
class Type:
    def __init__(self, name, effectiveAgainst, weakAgainst): # Constructor
        self.name = name
        self.effAgainst = effectiveAgainst
        self.weakAgainst = weakAgainst

    def loadJSON(self, ret): # Concatena esta instancia al JSON que se pasa como parámetro
        try:
            x = {
            "name":"{:1}".format(self.name),
            "effAgainst":"{:1}".format(self.effAgainst),
            "weakAgainst":"{:1}".format(self.weakAgainst)
            }
            ret += json.loads(x) 
            return ret
        except:
            return -1

    def getFromJSON(self, name, j): # Recibe el nombre y el JSON. Devuelve el Type, si lo encuentra
        t = Type(None, None, None)
        for typ in j["Type"]:
            if typ["name"] == name:
                t.name = typ["name"]
                t.effAgainst = typ["effAgainst"]
                t.weakAgainst = typ["weakAgainst"]
                break
        if t.name != None:
            return t
        else:
            return -1

    def isWeakAgainst(self, name, j):  # Devuelve True si encuentra al parámetro enviado en los tipos contra los que es débil
        typeJ = self.getFromJSON(name, j)
        if (typeJ in self.weakAgainst):
            return True
        else:
            return False
            
    def isEffAgainst(self, name, j):  # Devuelve True si encuentra el parámetro enviado en los tipos contra los que es efectivo
        typeJ = self.getFromJSON(name, j)
        if (typeJ in self.effAgainst):
            return True
        else:
            return False