# -*- coding: utf-8 -*-
import json
with open("cards.json") as archivo:
  datos = json.load(archivo)

# Ejercicio 1
tipo = []
for t in (datos):
  if t["type"] not in filtro:
    filtro.append(t["type"])

for i in tipo:
  if i !="HERO_POWER":
    if i !="CHEAT":
      if i !="HERO":
        print "\n", i
  for e in (datos):
    if e["type"] == i:
      if e["type"]!="HERO_POWER":
        if e["set"]!="CHEAT":
          if e["type"]!="HERO":
            print e["name"]

# Ejercicio 2
filtro3 = []
for m in (datos):
  if m.get("playerClass") == "NEUTRAL":
    filtro3.append(m.get("mechanics"))

contador = []
for f in filtro3:
  if f:
    contador.append(f[0])

mecanicas = []
for j in contador:
  if j not in mecanicas:
    print j, contador.count(j)
    mecanicas.append(j)
    
# Ejercicio 3
clase = raw_input("Clase jugable: ")
rareza = raw_input("Rareza: ")
for r in (datos):
  if r["type"]!="HERO_POWER":
    if r["set"]!="CHEAT":
      if r["type"]!="HERO":
        if r["playerClass"] == clase and r.get("rarity") == rareza:
          print r["name"]
# Ejercicio 4
