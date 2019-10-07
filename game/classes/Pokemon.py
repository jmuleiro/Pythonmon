import json
import random
import math
import Attack
import Type

class Pokemon:
    # Clase principal de Pokémones.
    # Para un pokemon nuevo, se debe ejecutar desde el init: 1.randomize 2.calcIVs, 3.normalize

    def __init__(self, name, descr, type1, type2, baseATK, baseDF, baseHP, path): # Constructor
        self.name = name
        self.descr = descr
        self.type1 = type1
        self.type2 = type2
        self.lvl = 0 # Nivel entre 0 y 100
        self.ivatk = 0 # ------ Individual Values ------
        self.ivdf = 0 # 0 <= x =< 31
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
        j = self.readJSON(path)
        self.randomize(j, "pokemon-project/json/types.json")
        self.calcIVs()
        self.normalize(True)

    def normalize(self, newPkmn): # Normalizar y calcular totalHP, totalATK, totalDF, currentHP, etc
        self.totalATK = math.floor(((self.baseATK + self.ivatk) * 2 + (math.sqrt(self.evATK) / 4)) * self.lvl / 100 + 5)
        self.totalDF = math.floor(((self.baseDF + self.ivdf) * 2 + (math.sqrt(self.ivdf) / 4)) * self.lvl / 100 + 5)
        self.totalHP = math.floor((((self.baseHP + self.ivhp) * 2 + (math.sqrt(self.evHP) / 4)) * self.lvl / 100 ) + self.lvl + 10)
        if (newPkmn):
            self.currentHP = self.totalHP

    def calcIVs(self): # Calcular IVS
        self.ivatk = random.randint(0,31)
        self.ivdf = random.randint(0,31)
        self.ivhp = random.randint(0,31)
    
    def getCaught(self): # Falta parám "pokeball" para el rate y status condition
        x = max(((3 * self.totalHP - 2 * self.currentHP) / (3 * self.totalHP)), 1) # catch rate
        r = random.randint(1, 255)
        if x > 255:
            x = 255
        if x == r:
            return True
        else:
            return False        

    def randomize(self, j, path): # Randomizar según el nombre. Falta criterio de cálculo de nivel
        j = j["Pokemon"]
        r = random.randint(1, len(j))
        self.name = j[r].name
        self.descr = j[r].descr
        self.type1 = Type.Type(j[r].type1, path)
        self.type2 = Type.Type(j[r].type2, path)
        self.baseATK = j[r].baseATK
        self.baseDF = j[r].baseDF
        self.baseHP = j[r].baseHP
        self.lvl = random.randint(20, 50) # Temp placeholder value <-----------------------------

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
            ret += json.dumps(x)
            return ret
        except:
            return -1
    
    def getFromJSON(self, name, j): # Recibe el nombre y JSON de Pkmn. Devuelve el objeto de la clase
        p = Pokemon(None, None, None, None, None, None, None, None)
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
            file.write(json.dumps(j)) # cambiar
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
        