#distância de haversine
from math import *

def haversine(r, laA, loA, laB, loB):
    la = (sin((laB - laA)/2))**2
    lo = (sin((loB - loA)/2))**2
    soma = la + cos(laA) * cos(laB) * lo
    d = 2*r * asin((soma)**0.5)
    return d


#sorteando países
import random

def sorteia_pais(p):
    paises = []
    for k in p.keys():
        paises.append(k)
    pais = random.choice(paises)
    return pais


#está na lista
def esta_na_lista(p, l):
    paises = []
    for i in l:
        paises.append(i[0])
    if p in paises:
        return True
    else:
        return False


#sorteia letra com restricoes
def sorteia_letra(p, rest):
    cesp =  ['.', ',', '-', ';', ' ']
    caract = []
    for c in p:
        if c not in cesp and c not in rest:
            caract.append(c)

    return random.choice(caract)


#normaliza base de países
def normaliza(d):
    saida = {}
    for pais in d.values():
        for k, v in pais.items():
            saida[k] = {}
            for key, value in v.items():
                saida[k][key] = value
            
    return saida


#add paises em lista ordenada
def adiciona_em_ordem(pais, distancia, lista_paisdistancia):
    lista = [pais, distancia]
    nova = []

    if len(lista_paisdistancia) == 0:
        nova.append(lista)

    for listas in lista_paisdistancia:
        if listas[1] > distancia and lista not in nova:
            nova.append(lista)
            nova.append(listas)
        elif listas[1] > distancia:
            nova.append(listas)
                        
                        
        elif listas[1] < distancia: 
            nova.append(listas)

    if lista not in nova:
        nova.append(lista)
            
    return nova