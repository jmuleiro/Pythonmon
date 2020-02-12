import json
import sys
import random
import math
import os.path
import Attack
import Type

class Pokemon:
    # Clase principal de Pokémones.
    # Para un pokemon nuevo, se debe ejecutar desde el init: 1.randomize 2.calcIVs, 3.normalize

    def __init__(self, name = None, descr = None, type1 = None, type2 = None, baseATK = None, baseDF = None, baseHP = None, dexnbr = None, path = None, doCalcs = None): # Constructor
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
        self.dexnbr = dexnbr
        self.totalATK = 0
        self.totalDF = 0
        self.totalHP = 0
        if doCalcs:
            j = readJSON(path)
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
            if ret == {}:
                ret = {
                "name":"{:1}".format(self.name),
                "descr":"{:1}".format(self.descr),
                "type1":"{:1}".format(self.type1),
                "type2":"{:1}".format(self.type2),
                "baseATK":"{:1}".format(self.baseATK),
                "baseDF":"{:1}".format(self.baseDF),
                "baseHP":"{:1}".format(self.baseHP)
                }
                ret = json.dumps(ret)
            else:
                x = {
                "name":"{:1}".format(self.name),
                "descr":"{:1}".format(self.descr),
                "type1":"{:1}".format(self.type1),
                "type2":"{:1}".format(self.type2),
                "baseATK":"{:1}".format(self.baseATK),
                "baseDF":"{:1}".format(self.baseDF),
                "baseHP":"{:1}".format(self.baseHP)
                }
                ret += json.dumps(x)
                print("funciono el dump")
            return ret
        except Exception as e:
            print("Pokemon class loadJSON method Failed:" + str(e) + ", in line {}".format(sys.exc_info()[-1].tb_lineno) + ", exception type: " + str(type(e)))
            return -1
    
    def getFromJSON(self, name, j): # Recibe el nombre y JSON de Pkmn. Devuelve el objeto de la clase
        try:
            p = Pokemon()
            js = j.split("}")
            for pkmn in js:
                pkmn += "}"
                pkmn = json.loads(pkmn)
                #print("pkmnname: " + pkmn["name"] + "  name: " + name)
                if pkmn["name"] == name:
                    p.name = pkmn["name"]
                    p.descr = pkmn["descr"]
                    p.type1 = pkmn["type1"]
                    p.type2 = pkmn["type2"]
                    p.baseATK = pkmn["baseATK"]
                    p.baseDF = pkmn["baseDF"]
                    p.baseHP = pkmn["baseHP"]
            if p.name != None:
                return p
            else:
                return -1
        except Exception as e:
            print("Pokemon class getFromJSON method (name, j) Failed: " + str(e) + ", in line {}".format(sys.exc_info()[-1].tb_lineno) + ", exception type: " + str(type(e)))
            return -1
    
def writeJSON(j, path): # Guarda el archivo JSON de Pkmn path: pokemon-project/json/pkmn.json
    try:
        if os.path.exists(path):
            jf = {}
            with open(path, "r") as file:
                jf = json.load(file)
            j = json.loads(j)
            jf += j
            
            with open(path, "w") as file:
                file.write(json.dumps(jf))
        else:
            p = Pokemon()
            c = 0
            js = j.split("}")
            for pkmn in js:
                pkmn += "}"
                print("pkmn: " + pkmn)
                pkmn = json.loads(pkmn)
                if c == 0:
                    print("hasta aca")
                    p = p.getFromJSON(pkmn["name"], j)
                    pkmn = "{" + "{:1}".format(p.name) + ":{" + "{:2}".format(p) + "}/}"
                else:
                    p = p.getFromJSON(pkmn["name"], j)
                    pkmn[len(pkmn)] = ","
                    pk2 = {"{:1}".format(p.name):{p}}
                    pkmn += pk2[1:len(pk2)]
                c += 1
            file = open(path, "w")
            file.write(j)
            file.close()
        return 1
    except Exception as e:
        print("Pokemon class writeJSON (j, path) method Failed:" + str(e) + ", in line {}".format(sys.exc_info()[-1].tb_lineno) + ", exception type: " + str(type(e)))
        return -1

def readJSON(path): # Lee y retorna el archivo JSON de Pkmn path: pokemon-project/json/pkmn.json
    try:
        file = open(path, "r")
        j = file.read(len(file))
        file.close()
        return json.loads(j)
    except Exception as e:
        print("readJSON (path) function Failed: " + str(e) + ", in line {}".format(sys.exc_info()[-1].tb_lineno) + ", exception type: " + str(type(e)))
        return -1
        