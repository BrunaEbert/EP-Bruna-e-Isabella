from funcoes import posicao_valida, define_posicoes, preenche_frota

lista=[["porta-aviões",4,1], ["navio-tanque",3,2], ["contratorpedeiro",2,3], ["submarino",1,4]]
frota={}

for i in range (len(lista)):
    for j in range (lista[i][2]):
        print(f"Insira as informações referentes ao navio {lista[i][0]} que possui tamanho {lista[i][1]}")
        linha=int(input())
        coluna=int(input())
        if lista[i][0]!="submarino":
            orientacao=int(input())
        else:
            orientacao=1
        if orientacao==1:
            orientacao="vertical"
        if orientacao==2:
            orientacao="horizontal"
        while posicao_valida( frota, linha, coluna, orientacao, lista[i][1])==False:
            print("Esta posição não está válida!")
            print(f"Insira as informações referentes ao navio {lista[i][0]} que possui tamanho {lista[i][1]}")
            linha=int(input())
            coluna=int(input())
            if lista[i][0]!="submarino":
                orientacao=int(input())
            else:
                orientacao=1
            if orientacao==1:
                orientacao="vertical"
            if orientacao==2:
                orientacao="horizontal"
        frota=preenche_frota(frota,lista[i][0],linha,coluna, orientacao, lista[i][1])

print(frota)


