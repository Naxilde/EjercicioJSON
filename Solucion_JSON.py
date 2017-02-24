# -*- coding: utf-8 -*-
import json
with open("cards.json") as archivo:
  datos = json.load(archivo)

#filtro = []
#for e in (datos):
#  if e["type"] not in filtro:
#    print e["type"]
#    filtro.append(e["type"])
for e in (datos):
  if e["type"]!="HERO_POWER":
    if e["set"]!="CHEAT":
      if e["playerClass"]=="PRIEST":
        print e["name"]
