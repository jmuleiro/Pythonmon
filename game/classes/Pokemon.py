import Type
import Attack
import json

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
    
    def getFromJSON(self, name, j):
        p = Pokemon(None, None, None, None, None, None, None, None)
        