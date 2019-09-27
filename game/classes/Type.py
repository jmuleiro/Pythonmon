import json

class Type:
    def __init__(self, name, effectiveAgainst, weakAgainst):
        self.name = name
        self.effAgainst = effectiveAgainst
        self.weakAgainst = weakAgainst
    def getTypeInfo(self, name): # Get type effective against & weak against by name
        pass
    def pushJSON(self, jsonT, name, effAgainst, weakAgainst): # Devuelve el JSON con el tipo que se pasó por parámetro agregado
        x = {
            "name":"{:1}".format(name),
            "effAgainst":"{:1}".format(effAgainst),
            "weakAgainst":"{:1}".format(weakAgainst)
        }
        jsonT += json.dumps(x)
        return jsonT
    def getFromJSON(self, name):
        x = json.load(name)
        return x
    def isWeakAgainst(self, name):
        typeJSON = getFromJSON(self, name)
        if (typeJSON in self.weakAgainst):
            return True
        else
            return False