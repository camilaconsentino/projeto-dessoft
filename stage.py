#front end EP2

from sympy import are_similar
import emoji

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
        print('___________DE__________') 
        print('_________DICAS_________')
        print('_______________________')

        print('1. Cor da bandeira --> custa 4 tentativas')
        print('2. Letra da capital -> custa 3 tentativas')
        print('3. Área -------------> custa 6 tentativas')
        print('4. População --------> custa 5 tentativas')
        print('5. Continente -------> custa 7 tentativas')
        print('0. Sem dicas --------> {0}' .format(emoji.emojize(':zipper_mouth_face')))

        dica = input('Escolha sua dica [0|1|2|3|4|5]: ')

        #cor da bandeira
        if dica == '1':
            if tentativas >= 4:
                tentativas -= 4
                verifica_cores = []
                cor_sorteada = sorteia_cor(bandeiras, verifica_cores, pais_sorteado)
                verifica_cores.append(cor_sorteada)
                print(f'Dica: {0}' .format(verifica_cores))

            else: #tentar ver o bang das cores
                print('Você não tem saldo! {0} \n' .format('\U0001F643'))
        
        #letra da capital
        elif dica == '2':
            if tentativas >= 3:
                tentativas -= 3
                letras_sorteadas = []
                capital = capitais[pais_sorteado]
                letra = sorteia_letra(capital, letras_sorteadas)
                letras_sorteadas.append(letra)
                print(f'Letra da capital: {0}' .format(letras_sorteadas))

            else: #tentar ver o bang das cores
                print('Você não tem saldo! {0} \n' .format('\U0001F643'))
        
        #area
        elif dica == '3':
            if tentativas >= 6:
                tentativas -= 6
                area = areas[pais_sorteado]
                print(f'Área do país é: {0}'.format(area))

            else: #tentar ver o bang das cores
                print('Você não tem saldo! {0} \n' .format('\U0001F643'))

        #populacao
        elif dica == '4':
            if tentativas >= 5:
                tentativas -= 5
                populacao = populacoes[pais_sorteado]
                print(f'A população do país é: {0}' .format(populacao))
            
            else: #tentar ver o bang das cores
                print('Você não tem saldo! {0} \n' .format('\U0001F643'))

        #continente
        elif dica == '5':
            if tentativas >= 7:
                tentativas -= 7
                continente = continentes[pais_sorteado]
                print(f'O continente do país é: {0}'.format(continente))
            
            else: #tentar ver o bang das cores
                print('Você não tem saldo! {0} \n' .format('\U0001F643'))


    elif comando == 'inventario':
        print('Você ainda tem {0} tentativas! {1}' .format(tentativas, '\U0001F618') 

    elif comando == 'desistir':
        continuar = False

    elif comando == pais_sorteado:
        print('Você acertou! {0}' .format('\U0001F606'))
        repete = input('Jogar novamente [s|n]? {0}' .format('\U0001F60D'))

        if repete == 's':
            continuar

        else: 
            continuar = False

    elif comando not in paises:
        print('Esse pais não existe {0}' .format('\U0001F928'))
        
    
    else:
        palpites_anteriores = [] 
        distancia = haversine(raio, latitudes[pais_sorteado], longitudes[pais_sorteado], latitudes[comando], longitudes[comando])
        esta_na_lista = esta_na_lista(comando, palpites_anteriores)

        if esta_na_lista == True:
            print('Voce já tentou esse país! {0}' .format('\U0001F644'))

        else:
            palpites_anteriores = adiciona_em_ordem(comando, distancia, palpites_anteriores)
            for palpite in palpites_anteriores:
                print(f' pais: {0} -> distancia: {1}' .format(palpite[0], palpite[1]))


    comando = input('Chute um país! {0}\n' .format('\U0001F929'))





