################################################################################################

import random 

# Funções do jogo:

def define_posicoes(linha, coluna, orientacao, tamanho):
    posições = []
    if orientacao == "horizontal":
        coluna -= 1
        for x in range(tamanho):
            coluna +=1
            posição = [linha, coluna]
            posições.append(posição)
    if orientacao == "vertical":
        linha -= 1
        for x in range(tamanho):
            linha +=1
            posição = [linha, coluna]
            posições.append(posição)

    return posições

#----------------------------------------------------------------------------#

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    posição = [define_posicoes(linha, coluna, orientacao, tamanho)]

    if nome_navio in frota:
        frota[nome_navio] += posição
    else:
        frota[nome_navio] = posição

    return frota

#------------------------------------------------------------------------------#

def faz_jogada(tabuleiro, linha, coluna):
    chute = tabuleiro[linha][coluna]
    if chute == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

#------------------------------------------------------------------------------#

def posiciona_frota(frota):
    tabuleiro = [[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]]
    for navios in frota.values():
        for lista1 in navios:
            for posicao in lista1:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro

#------------------------------------------------------------------------------#

def afundados(frota, tabuleiro):
    derrubados = 0
    for navios in frota.values():
        for lista1 in navios:
            tamanho = len(lista1)
            x = 0
            for posicao in lista1:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] == 'X':
                    x += 1
            if x == tamanho:
                derrubados += 1
    
    return derrubados

#------------------------------------------------------------------------------#

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    posicoes_ocupadas = []
    

    for navios in frota.values():
        for lista1 in navios:
            for posicao in lista1:
                posicoes_ocupadas.append(posicao)
    
    for lugar in posicoes:
        linha1 = lugar[0]
        coluna1 = lugar[1]
        if linha1 > 9 or linha1 < 0 or coluna1 > 9 or coluna1 < 0:
            return False
        if lugar in posicoes_ocupadas:
            return False
    return True

#------------------------------------------------------------------------------#

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

################################################################################################

# Posicionando Frota:

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

for embarcacao in frota:
    lista_embarcacoes = list(frota.keys())
    tamanho = len(frota) - lista_embarcacoes.index(embarcacao)
    n_embarcacoes = lista_embarcacoes.index(embarcacao) + 1
    n = 1
    while n <= n_embarcacoes:
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(embarcacao, tamanho))
        linha  = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if embarcacao == 'submarino':
            orientacao = 'vertical'
        else:
            orientacao = int(input('[1] Vertical [2] Horizontal >'))
            if orientacao == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'
        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
            frota_jogador = preenche_frota(frota, embarcacao, linha, coluna, orientacao, tamanho)
            n += 1 
        else:
            print('Esta posição não está válida!')

##print(frota_jogador)

# Jogadas do Jogador:

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota_jogador)

posicoes_ataque_informadas = []
posicoes_defesa_sorteadas = []

jogando = True

while jogando:

    # Monta tabuleiro:
    tabuleiro_jogo = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(tabuleiro_jogo)

    # Insere coordenadas do ataque:
    bol_1 = True
    while bol_1:
        linha_ataque = int(input('Qual linha deseja atacar? '))
        if linha_ataque < 0 or linha_ataque > 9:
            print('Linha inválida!')
        else:
            bol_1 = False
    
    bol_2 = True
    while bol_2:
        coluna_ataque = int(input('Qual coluna deseja atacar? '))
        if coluna_ataque < 0 or coluna_ataque > 9:
            print('Coluna inválida!')
        else:
            bol_2 = False 

    posicao_ataque = [linha_ataque, coluna_ataque]

    # Confere se a coordenanda de ataque informada já foi informada:
    if posicao_ataque in posicoes_ataque_informadas:

        posicoes_ataque_informadas.append(posicao_ataque)
        print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_ataque, coluna_ataque))
    
    # Caso o ataque seja válido, atualiza o tabuleiro:
    else:

        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)
        embarcacoes_afundadas = afundados(frota_oponente, tabuleiro_oponente)

        # Confere se o jogador ganhou
        if embarcacoes_afundadas == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False
        else:
            jogada_oponente = True 
            while jogada_oponente:
                linha_defesa = random.randint(0,9)
                coluna_defesa = random.randint(0,9)
                posicao_defesa = [linha_defesa, coluna_defesa]
                if posicao_defesa not in posicoes_defesa_sorteadas:
                    jogada_oponente = False
            print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_defesa, coluna_defesa))
            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_defesa, coluna_defesa)
            embarcacoes_afundadas_jogador = afundados(frota_jogador, tabuleiro_jogador)
            if embarcacoes_afundadas_jogador == 10:
                print('Xi! O oponente derrubou toda a sua frota =(')
                jogando = False