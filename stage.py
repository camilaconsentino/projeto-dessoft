#front end EP2

from sympy import are_similar


print('------------------------')
print('|                      |')
print('|         QUIZ         |')
print('|        PAÍSES        |')
print('|                      |')
print('------------------------')


print('COMANDOS:')
print('dica ---------- entra no mercado de dicas')
print('desistir ------ sai da rodada atual')
print('inventario ---- mostra sua posicao')

continuar = True
comando = input('Qual o seu palpite? ')

tentativas = 20

while continuar:

    if comando == 'dica':
        print('_______________________')
        print('________MERCADO________')
        print('___________DE__________') #acabar depois
        print('_________DICAS_________')
        print('_______________________')

        dica = input('Escolha sua dica: [0|1|2|3|4|5]: ')

        #cor da bandeira
        if dica == '1':
            if tentativas >= 4:
                tentativas -= 4
                verifica_cores = []
                cor_sorteada = sorteia_cor(bandeiras, verifica_cores, pais_sorteado)
                verifica_cores.append(cor_sorteada)
                print(f'Dica: {0}' .format(verifica_cores))

            else: #tentar ver o bang das cores
                print('Você não tem saldo!\n')
        
        #letra da capital
        elif dica == '2':
            if tentativas >= 3:
                tentativas -= 3
                letras_sorteadas = []
                capital = ''
                for pais, cap in capitais.items():
                    if pais == pais_sorteado:
                        capital = cap
                letra = sorteia_letra(capital, letras_sorteadas)
                letras_sorteadas.append(letra)
                print(f'Letra da capital: {0}' .format(letras_sorteadas))

            else: #cores no mercado de dicas
                print('Você não tem saldo!\n')
        
        #area
        elif dica == '3':
            if tentativas >= 6:
                tentativas -= 6
                area = dados[pais_sorteado]['area']
                print(f'Área do país é: {1}'.format(area))

            else:
                print('Você não tem saldo!\n')

        #populacao
        elif dica == '4':
            if tentativas >= 5:
                tentativas -= 5
                populacao = dados[pais_sorteado]['populacao']
                print(f)



    elif comando == 'inventario':
        print(tentativas) 

    elif comando == 'desistir':
        continuar = False

    elif comando == pais_sorteado:
        print('Voce acertou!')
        repete = input('Jogar novamente [s|n]?  ')

        if repete == 's':
            continuar

        else: 
            continuar = False

    elif comando not in paises:
        print('Esse pais não existe :/ ')
        
    
    else:
        palpites_anteriores = [] 
        distancia = haversine(raio, latitudes[pais_sorteado], longitudes[pais_sorteado], latitudes[comando], longitudes[comando])
        esta_na_lista = esta_na_lista(comando, palpites_anteriores)

        if esta_na_lista == True:
            print('Voce já tentou esse país!')

        else:
            palpites_anteriores = adiciona_em_ordem(comando, distancia, palpites_anteriores)
            for palpite in palpites_anteriores:
                print(f' pais: {0} -> distancia: {1}' .format(palpite[0], palpite[1]))



    comando = input('Chute um país! \n')





