def define_posicoes (linha,coluna,orientacao,tamanho):
    lista1=[]
    if orientacao=="vertical":
        for i in range(tamanho):
            lista1.append([linha+i,coluna])
    if orientacao=="horizontal":
        for i in range(tamanho):
            lista1.append([linha,coluna+i])
    return lista1
def preenche_frota(dfrota,nnavio,linha,coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nnavio in dfrota:
        dfrota[nnavio].append(posicoes)
    else:
        dfrota[nnavio] = [posicoes]
    return dfrota
def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]="X"
    if tabuleiro[linha][coluna]==0:
            tabuleiro[linha][coluna]="-"
    return tabuleiro