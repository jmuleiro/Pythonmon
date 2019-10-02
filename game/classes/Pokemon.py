import json
import Attack
import Type

class Pokemon:
    # Clase principal de Pokémones.
    
    def __init__(self, name, descr, type1, type2, lvl, atk, df, hp): # Constructor
        self.name = name
        self.descr = descr
        self.type1 = type1
        self.type2 = type2
        self.lvl = lvl # 0 >= x =< 100
        self.atk = atk # 0 >= x =< 15
        self.df = df # 0 >= x =< 15
        self.hp = hp # 0 >= x =< 15

    def randomize(self): # Randomizar
        pass

    def loadJSON(self, ret): # Carga a la variable JSON esta instancia de Pokémon
        try:
            x = {
                "name":"{:1}".format(self.name),
                "descr":"{:}".format(self.descr),
                "type1":"{:1}".format(self.type1.name),
                "type2":"{:1}".format(self.type2.name),
                "lvl":"{:1}".format(self.lvl),
                "atk":"{:1}".format(self.atk),
                "df":"{:1}".format(self.df),
                "hp":"{:1}".format(self.hp)
            }
            ret += json.loads(x)
            return ret
        except:
            return -1
    
    def getFromJSON(self, name, j): # Recibe el nombre y JSON de Pkmn. Devuelve el objeto de la clase
        p = Pokemon(None, None, None, None, None, None, None, None)
        for pkmn in j["Pokemon"]:
            p.name = pkmn["name"]
            p.descr = pkmn["descr"]
            p.type1 = pkmn["type1"].name
            p.type2 = pkmn["type2"].name
            p.lvl = pkmn["lvl"]
            p.atk = pkmn["atk"]
            p.df = pkmn["df"]
            p.hp = pkmn["hp"]
        if p.name != None:
            return p
        else:
            return -1
    
    def writeJSON(self, j): # Guarda el archivo JSON de Pkmn
        try:
            file = open("pokemon-project/json/pkmn.json", "w")
            file.write(j)
            file.close()
            return 1
        except:
            return -1

    def readJSON(self): # Lee y retorna el archivo JSON de Pkmn
        try:
            file = open("pokemon-project/json/pkmn.json", "r")
            j = file.read(len(file))
            file.close()
            return j
        except:
            return -1