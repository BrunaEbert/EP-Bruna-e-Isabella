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
def posiciona_frota(frota):
    tabuleiro=[]
    for i in range(10):
        linha=[]
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                linha= posicao[0]
                coluna= posicao[1]
                tabuleiro[linha][coluna] =1
    return tabuleiro
def afundados (frota,tabuleiro):
    soma=0
    for navio in frota.values():
        for i in navio:
            atingidas=0
            for j in i:
                linha=j[0]
                coluna=j[1]
                if tabuleiro[linha][coluna]=="X":
                    atingidas+=1
            if atingidas==(len(i)):
                soma+=1
    return soma
def posicao_valida( frota, linha, coluna, orientacao, tamanho):
    posicoes= define_posicoes(linha,coluna, orientacao, tamanho)
    for posicao in posicoes:
        l=posicao[0]
        c=posicao[1]
        if l<0 or l>9 or c<0 or c>9:
            return False
        for nome_navio in frota:
            for navio in frota[nome_navio]:
                for p in navio:
                    if p[0] ==l and p[1] == c:
                        return False
    return True