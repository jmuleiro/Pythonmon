import json
import sys
sys.path.append(sys.path[0] + "\\classes\\")
import Pokemon

def readJSON(self, path): # Path: pythonmon-master/json/console.json
    try:
        with open(path, "r") as fp:
            return json.load(fp)
    except:
        return -1

# ------------------------------- CONSOLA PRUEBAS & CARGA DE JSON -------------------------------
# Comandos: /create /save
jpkmn, i = ""
path = sys.path[0]
path.replace("\\", "/")
jtxt = readJSON(None, path + "/json/console.json")
while i != "/close":
    print("Qué desea hacer?")
    print("Opciones: Crear: /create")
    i = input().lower()
    if i == "/create":
        print(jtxt["createh"])
    elif i[0:8] == "/create ":
        print(jtxt["createerror"])
    elif i == "/create pokemon":
        print(jtxt["pkmnname"])
        name = input().lower()
        name = name[0].upper() + name[1:len(name) - 1].lower()
        print(jtxt["pkmndescr"])
        descr = input()
        print(jtxt["pkmntype1"])
        type1 = input().lower()
        print(jtxt["pkmntype2"])
        type2 = input().lower()
        print(jtxt["pkmnbaseatk"])
        baseatk = input()
        print(jtxt["pkmnbasedf"])
        basedf = input()
        print(jtxt["pkmnbasehp"])
        basehp = input()
        pkmn = Pokemon.Pokemon(name, descr, type1, type2, baseatk, basedf, basehp, path + "/json/pkmn.json")
        jpkmn = pkmn.loadJSON(jpkmn)