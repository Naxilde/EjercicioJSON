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
autor = raw_input("Autor: ")
f_rareza = []
rarezas = []
lista = []
for h in (datos):
  if h["type"]!="HERO_POWER":
    if h["set"]!="CHEAT":
      if h["type"]!="HERO":
        if h.get("rarity"):
          if h.get("artist") == autor:
            if h.get("name"):
	            lista2 = []
	            rarezas.append(h["rarity"])
              lista2.append(h["rarity"])
              lista2.append(h["name"])
	            lista.append(lista2)

for o in rarezas:
  if o not in f_rareza:
    print "\n", o, rarezas.count(o)
    for l in lista:
      if l[0] == o:
	print l[1]
    f_rareza.append(o)

# Ejercicio 5
clase1 = raw_input("Clase: ")
for w in (datos):
  if w["type"] == "HERO_POWER":
    if w.get("playerClass") == clase1:
      if w["set"] == "CORE":
        print "\n", w["playerClass"], w["name"], w["text"]

for u in filtro:
  if u !="HERO_POWER":
    if u !="CHEAT":
      if u !="HERO":
        print "\n", u
  c_cartas = []
  for q in (datos):
    if q["type"]== u:
      if q.get("playerClass") == clase1:
        if q["type"]!="HERO_POWER":
          if q["set"]!="CHEAT":
            if q["type"]!="HERO":
              c_cartas.append(q["name"])
  print len(c_cartas)

filtro2 = []
for n in (datos):
  if n.get("playerClass") == clase1:
    filtro2.append(n.get("mechanics"))
contador2 = []
for z in filtro2:
  if z and z[0] not in contador2:
    contador2.append(z[0])

otros = []
for s in (datos):
  if s.get("playerClass") != clase1:
    if s.get("playerClass") != "NEUTRAL":
      otros.append(s.get("mechanics"))
otros2 = []
for k in otros:
  if k and k[0] not in otros2:
    otros2.append(k[0])
for v in contador2:
 if v not in otros2:
  print "Mecanica:", v
