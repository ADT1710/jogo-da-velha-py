import time

from jogador import JogadorHumano, JogadorComputador

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [" " for _ in range(9)]
        self.vencedor_atual = None

    def printa_tabuleiro(self):
        for linha in [self.tabuleiro[i * 3: (i + 1) * 3] for i in range(3)]:
            print("| " + " |".join(linha) + " |")

    @staticmethod
    def printa_numeros_tabuleiro():
        numero_tabuleiro = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for linha in numero_tabuleiro:
            print("| " + " |".join(linha) + " |")

    def movimentos_disponiveis(self):
        movimentos = []
        for (i,local) in enumerate(self.tabuleiro):
            if local == " ":
                movimentos.append(1)
        return movimentos

    def quadrados_vazios(self):
        return " " in self.tabuleiro

    def numeros_quadrados_vazios(self):
        return self.tabuleiro.count(' ')

    def faz_movimento(self,quadrado,letra):
        if self.tabuleiro[quadrado] == ' ':
            self.tabuleiro[quadrado] = letra
            if self.vencedor(quadrado, letra):
                self.vencedor_atual = letra
            return True
        return False

    def vencedor(self,quadrado,letra):
        linha_ind = quadrado // 3
        linha = self.tabuleiro[linha_ind * 3: (linha_ind + 1) * 3]
        if all([local == letra for local in linha]):
            return True

        coluna_ind = quadrado % 3
        coluna = [self.tabuleiro[coluna_ind + i * 3] for i in range(3)]
        if all([local == letra for local in coluna]):
            return True

        if quadrado % 2 == 0:
            diagonal1 =[self.tabuleiro[i] for i in [0,4,8]]
            if all([local == letra for local in diagonal1]):
                return True
            diagonal2 = [self.tabuleiro[i] for i in [2, 4, 6]]
            if all([local == letra for local in diagonal2]):
                return True

        return False

def jogar(jogo, jogador_x, jogador_o, printa_jogo=True):
    if printa_jogo:
        jogo.printa_numeros_tabuleiro()

    letra = 'X'
    while jogo.quadrados_vazios():
        if letra == 'O':
            quadrado = jogador_o.pega_movimento(jogo)
        else:
            quadrado = jogador_x.pega_movimento(jogo)

        if jogo.faz_movimento(quadrado,letra):
            if printa_jogo:
                print(f'{letra} fez um movimento para o quadrado {quadrado}')
                jogo.printa_tabuleiro
                print('')

            if jogo.vencedor_atual:
                if printa_jogo:
                    print(f'{letra} venceu!')
                return letra


            letra = 'O' if letra == 'X' else 'X'

        time.sleep(0.8)

    if printa_jogo:
        print("É um Empate!")

if __name__ == "__main__":
    jogador_x = JogadorHumano('X')
    jogador_o = JogadorComputador('O')
    t = JogoDaVelha()
    jogar(t, jogador_x, jogador_o, printa_jogo=True)