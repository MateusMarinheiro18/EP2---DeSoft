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

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    posição = [define_posicoes(linha, coluna, orientacao, tamanho)]

    if nome_navio in frota:
        frota[nome_navio] += posição
    else:
        frota[nome_navio] = posição
    return frota 

def faz_jogada(tabuleiro, linha, coluna):
    chute = tabuleiro[linha][coluna]
    if chute == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]]
    for navios in frota.values():
        for lista1 in navios:
            for posicao in lista1:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro

