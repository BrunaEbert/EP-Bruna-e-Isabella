def define_posicoes (linha,coluna,orientacao,tamanho):
    lista1=[]
    if orientacao=="vertical":
        for i in range(tamanho):
            lista1.append([linha+i,coluna])
    if orientacao=="horizontal":
        for i in range(tamanho):
            lista1.append([linha,coluna+i])
    return lista1