# -*- coding: utf-8 -*-
import json
with open("cards.json") as archivo:
  datos = json.load(archivo)

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
