#front end EP2
#import emoji
from math import *
import random
from funcoes import normaliza, haversine, sorteia_pais, esta_na_lista, sorteia_letra, adiciona_em_ordem, sorteia_cor
from dicionario import hacker

#definindo variaveis
a = ''
dados_iniciais = hacker(a)

#raio
raio = 6371

#tentativas
tentativas = 20

#normalizando base:
dados_paises = normaliza(dados_iniciais)

#país sorteado:
pais_sorteado = sorteia_pais(dados_paises)

#palpites anteriores
palpites_anteriores = []

#verifica cores:
verifica_cores = []

#letras
letras_sorteadas = []

#para nao repetir dicas
dicas_repetidas = []

#criando dicionarios
paises = []
bandeiras = {}
capitais = {}
areas = {}
populacoes = {}
continentes = {}
latitudes = {}
longitudes = {}

for pais, dados in dados_paises.items():
    paises.append(pais)
    areas[pais] = dados['area']
    populacoes[pais] = dados['populacao']
    capitais[pais] = dados['capital']
    latitudes[pais] = dados['geo']['latitude']
    longitudes[pais] = dados['geo']['longitude']
    continentes[pais] = dados['continente']
    bandeiras[pais] = []
    for cor, value in dados['bandeira'].items():
        if value != 0:
            bandeiras[pais].append(cor)

print(capitais)
capital = capitais[pais_sorteado]
print(capital)

#inicializando            

print('------------------------')
print('|                      |')
print('|         QUIZ         |')
print('|        PAÍSES        |')
print('|                      |')
print('------------------------')


print('\nCOMANDOS:')
print('\ndica ------------ entra no mercado de dicas')
print('desistir -------- sai da rodada atual')
print('inventario ------ mostra sua posicao\n')


continuar = True
comando = input('\nChute um país!{0} ' .format('\U0001F929'))



while continuar:

    if tentativas == 1:
        print('\nAcabaram suas tentativas! O país correto era {0}\n' .format(pais_sorteado))
        break

    if comando == 'dica':
        print('\nMERCADO DE DICAS')        
        print('------------------------------------------')
        print('1. Cor da bandeira --> custa 4 tentativas')
        print('2. Letra da capital -> custa 3 tentativas')
        print('3. Área -------------> custa 6 tentativas')
        print('4. População --------> custa 5 tentativas')
        print('5. Continente -------> custa 7 tentativas')
        print('0. Sem dicas --------> {0}               ' .format('\U0001F910'))
        print('------------------------------------------')

        dica = input('\nEscolha sua dica [0|1|2|3|4|5]: ')

        #cor da bandeira
        if dica == '1':
            if tentativas >= 4:
                tentativas -= 4
                verifica_cores = sorteia_cor(bandeiras, verifica_cores, pais_sorteado)
                print('Dica: {0}' .format(verifica_cores))

            else: #tentar ver o bang das cores
                print('\nVocê não tem saldo!{0}' .format('\U0001F643'))
        
        #letra da capital
        elif dica == '2':
            if tentativas >= 3:
                tentativas -= 3
                capital = capitais[pais_sorteado]
                letra = sorteia_letra(capital, letras_sorteadas)
                letras_sorteadas.append(letra)
                print('\nLetra da capital: {0}' .format(letras_sorteadas))

            else: #tentar ver o bang das cores
                print('\nVocê não tem saldo!{0}' .format('\U0001F643'))
        
        #area
        elif dica == '3':
            if tentativas >= 6:
                area = areas[pais_sorteado]
                if dica not in dicas_repetidas:
                    tentativas -= 6
                    dicas_repetidas.append(dica)

                print('\nÁrea do país é: {0}km2'.format(area))

            else: #tentar ver o bang das cores
                print('\nVocê não tem saldo!{0}' .format('\U0001F643'))

        #populacao
        elif dica == '4':
            if tentativas >= 5:
                populacao = populacoes[pais_sorteado]
                if dica not in dicas_repetidas:
                    tentativas -= 5
                    dicas_repetidas.append(dica)
                
                print('\nA população do país é: {0} habitantes' .format(populacao))
            
            else: #tentar ver o bang das cores
                print('\nVocê não tem saldo!{0}' .format('\U0001F643'))

        #continente
        elif dica == '5':
            if tentativas >= 7:
                continente = continentes[pais_sorteado]
                if dica not in dicas_repetidas:
                    tentativas -= 7
                    dicas_repetidas.append(dica)
                
                print('\nO continente do país é: {0}'.format(continente))
            
            else: #tentar ver o bang das cores
                print('\nVocê não tem saldo!{0}' .format('\U0001F643'))

    elif comando == 'inventario':
        print('\nVocê ainda tem {0} tentativas!{1}' .format(tentativas, '\U0001F618')) 

    elif comando == 'desistir':
        print('\nAté mais!\n')
        break

    elif comando == pais_sorteado:
        print('Você acertou!{0}' .format('\U0001F606'))
        repete = input('\nJogar novamente [s|n]?{0}' .format('\U0001F60D'))

        if repete == 's':
            continuar

        else: 
            continuar = False
    
    elif comando not in paises:
        print('\nEsse pais não existe{0}' .format('\U0001F928'))    

    else:
        distancia = haversine(raio, latitudes[pais_sorteado], longitudes[pais_sorteado], latitudes[comando], longitudes[comando])
        palpite = [comando, distancia]
        estanalista = esta_na_lista(palpite, palpites_anteriores)
        if estanalista == True:
            print('\nVocê já tentou esse país!{0}' .format('\U0001F644'))
        else:
            palpites_anteriores = adiciona_em_ordem(comando, distancia, palpites_anteriores)
            tentativas -= 1
            for palpite in palpites_anteriores:
                dis = palpite[1]
                nome = palpite[0]
                print('\nPaís: {0} -> Distância: {1:,.0f}km' .format(nome, dis))

    comando = input('\nChute um país!{0} ' .format('\U0001F929'))
