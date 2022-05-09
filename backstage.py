#raio
raio = 6371

#tentativas
tentativas = 20

#normalizando base:
dados_paises = normaliza(dados_iniciais)

#país sorteado:
pais_sorteado = sorteia_pais(dados_paises)

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


