tabuleiro = [1,2,3,4,5,6,7,8,9]
jogador_atual = "X"
jogadas_feitas = 0

def exibir_tabuleiro():
    print(tabuleiro[0],"|",tabuleiro[1],"|",tabuleiro[2])
    print("---""---""---")
    print(tabuleiro[3],"|",tabuleiro[4],"|",tabuleiro[5])
    print("---""---""---")
    print(tabuleiro[6],"|",tabuleiro[7],"|",tabuleiro[8])

def verificar_vencedor(jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for c in combinacoes:
        if tabuleiro[c[0]] == jogador and tabuleiro[c[1]] == jogador and tabuleiro[c[2]] == jogador:
            return True
    return False


while jogadas_feitas < 9:
    exibir_tabuleiro()

    posicao = int(input("Escolha uma posição: ",))

    if posicao < 1 or posicao >9:
        print("Posição inválida")
    
    elif tabuleiro[posicao - 1] == "X" or tabuleiro[posicao - 1] == "O":
        print("Posição ocupada! Escolha outra posição")  
    else:
        tabuleiro[posicao - 1] = jogador_atual

        jogadas_feitas += 1
            
        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"


print("Fim de Jogo!")
exibir_tabuleiro  

   
    



