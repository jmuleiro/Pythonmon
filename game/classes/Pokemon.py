import json
import random
import math
import Attack
import Type

class Pokemon:
    # Clase principal de Pokémones.
    # Para un pokemon nuevo, se debe ejecutar desde el init: 1.randomize 2.calcIVs, 3.normalize

    def __init__(self, name, descr, type1, type2, baseATK, baseDF, baseHP): # Constructor
        self.name = name
        self.descr = descr
        self.type1 = type1
        self.type2 = type2
        self.lvl = 0 # Nivel entre 0 y 100
        self.ivatk = 0 # ------ Individual Values ------
        self.ivdf = 0 # 0 <= x =< 15
        self.ivhp = 0 # --------------------------------
        self.currentHP = 0
        self.evATK = 0 # ------ Effort Values ------
        self.evDF = 0 # 0 <= x <= 100 ó 255
        self.evHP = 0 # ----------------------------
        self.baseATK = baseATK
        self.baseDF = baseDF
        self.baseHP = baseHP
        self.totalATK = 0
        self.totalDF = 0
        self.totalHP = 0

    def normalize(self): # Normalizar y calcular totalHP, totalATK, totalDF, currentHP, etc
        pass

    def calcIVs(self): # Calcular IVS
        pass
    
    def getCaught(self): # Falta parám "pokeball" para el rate
        pass

    def randomize(self, path): # Randomizar según el nombre, rehacer función
        j = json.loads(self.readJSON(path))
        r = random.randint(1, len(j))
        self = j[r]

    def loadJSON(self, ret): # Carga a la variable JSON esta instancia de Pokémon
        try:                 # Re-ver los parámetros que se guardan.
            x = {
                "name":"{:1}".format(self.name),
                "descr":"{:1}".format(self.descr),
                "type1":"{:1}".format(self.type1.name),
                "type2":"{:1}".format(self.type2.name),
                "baseATK":"{:1}".format(self.baseATK),
                "baseDF":"{:1}".format(self.baseDF),
                "baseHP":"{:1}".format(self.baseHP)
            }
            ret += json.loads(x)
            return ret
        except:
            return -1
    
    def getFromJSON(self, name, j): # Recibe el nombre y JSON de Pkmn. Devuelve el objeto de la clase
        p = Pokemon(None, None, None, None, None, None, None)
        for pkmn in j["Pokemon"]:
            if pkmn["name"] == name:
                p.name = pkmn["name"]
                p.descr = pkmn["descr"]
                p.type1 = pkmn["type1"].name
                p.type2 = pkmn["type2"].name
                p.baseATK = pkmn["baseATK"]
                p.baseDF = pkmn["baseDF"]
                p.baseHP = pkmn["baseHP"]
        if p.name != None:
            return p
        else:
            return -1
    
    def writeJSON(self, j, path): # Guarda el archivo JSON de Pkmn path: pokemon-project/json/pkmn.json
        try:
            file = open(path, "w")
            file.write(json.dumps(j))
            file.close()
            return 1
        except:
            return -1

    def readJSON(self, path): # Lee y retorna el archivo JSON de Pkmn path: pokemon-project/json/pkmn.json
        try:
            file = open(path, "r")
            j = file.read(len(file))
            file.close()
            return json.loads(j)
        except:
            return -1
        