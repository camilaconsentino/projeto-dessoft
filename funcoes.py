#bibliotecas 
from math import *
import random

#distância de haversine
def haversine(r, laA, loA, laB, loB):
    la = (sin((laB - laA)/2))**2
    lo = (sin((loB - loA)/2))**2
    soma = la + cos(laA) * cos(laB) * lo
    d = 2*r * asin((soma)**0.5)
    return d


#sorteando países
def sorteia_pais(p):
    paises = []
    for k in p.keys():
        paises.append(k)
    pais = random.choice(paises)
    return pais


#está na lista
def esta_na_lista(palpite, palpites_anteriores):
    if palpite in palpites_anteriores:
        return True
    else:
        return False
# se retornar True, print 'voce ja tentou esse pais' e print comando dnv (e nao perde uma tentativa)
# se retornar False, chamamos a funcao adiciona_em_ordem


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
    for continente, pais in d.items():
        for k, v in pais.items():
            saida[k] = {}
            for key, value in v.items():
                saida[k][key] = value
            saida[k]['continente'] = continente
    return saida


#add paises em lista ordenada
def adiciona_em_ordem(palpite, distancia, palpites_anteriores):
    lista = [palpite, distancia]
    nova = []

    if len(palpites_anteriores) == 0:
        nova.append(lista)

    for listas in palpites_anteriores:
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


#função para sortear cor da bandeira
def sorteia_cor(dicband, verificacores, paissorteado):
    for pais, cores in dicband.items():
        if pais == paissorteado:
            cor = random.choice(cores)
            while cor in verificacores:
                cor = random.choice(cores)
            verificacores.append(cor)
            
            return verificacores

