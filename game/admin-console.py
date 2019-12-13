import json
import sys
sys.path.append(sys.path[0] + "\\classes\\")
import Pokemon
import Type

def readJSON(self, path): # Path: pythonmon-master/json/console.json
    try:
        with open(path, "r") as fp:
            return json.load(fp)
    except:
        return -1

# ------------------------------- CONSOLA PRUEBAS & CARGA DE JSON -------------------------------
# Comandos: /create /save
jpkmn = {}
i = ""
path = sys.path[0]
path.replace("\\", "/")
jtxt = readJSON(None, path + "/json/console.json")
while i != "/close":
    print("Qué desea hacer?")
    print("Comandos: \n/create /save")
    i = input().lower()
    if i == "/create help":
        print(jtxt["createh"])
    elif i == "/create pokemon":
        print(jtxt["pkmnname"])
        name = input().lower()
        name = name[0].upper() + name[1:len(name)].lower()
        print(jtxt["pkmndescr"])
        descr = input()
        print(jtxt["pkmntype1"]) # Falta búsqueda y validación con el JSON de types
        type1 = input().lower()
        print(jtxt["pkmntype2"]) # Falta búsqueda y validación con el JSON de types
        type2 = input().lower()
        if type2 == "":
            type2 = " "
        print(jtxt["pkmnbaseatk"])
        baseatk = input()
        print(jtxt["pkmnbasedf"])
        basedf = input()
        print(jtxt["pkmnbasehp"])
        basehp = input()
        print(jtxt["pkmndexnbr"])
        dexnbr = input()
        pkmn = Pokemon.Pokemon(name, descr, type1, type2, baseatk, basedf, basehp, dexnbr, None, False)
        jpkmn = pkmn.loadJSON(jpkmn)
        print(jpkmn)
    elif i == "/create type":
        pass
    elif i == "/create pokeball":
        pass
    elif i == "/create attack":
        pass
    elif i[0:8] == "/create ":
        print(jtxt["createerror"])
    elif i[0:7] == "/create":
        print(jtxt["createerror"])
    elif i == "/save help":
        print(jtxt["saveh"])
    elif i == "/save pokemon":
        if jpkmn == "":
            print(jtxt["saveerror2"].format("Pokémon"))
        else:
            print(Pokemon.writeJSON(jpkmn, path + "/json/pkmn.json"))
    elif i[0:6] == "/save ":
        print(jtxt["saveerror"])
    elif i[0:5] == "/save":
        print(jtxt["saveerror"])