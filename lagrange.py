# lagrange.py

import itertools
import math

import matplotlib.pyplot
import numpy as np
import vector


class SistemaLagrange:
    def __init__(self, tamanho):
        # Inicializa o sistema Lagrange com um tamanho específico
        self.tamanho = tamanho
        self.corpos = []

        # Cria a figura e o eixo 3D para visualização
        self.figura, self.eixo = matplotlib.pyplot.subplots(
            1,
            1,
            figsize = (self.tamanho / 50, self.tamanho / 50),
            subplot_kw = {"projection": "3d"},
        )
        self.eixo.view_init(0, 0)
        self.figura.tight_layout()

    def adicionar_corpo(self, corpo):
        # Adiciona um corpo ao sistema Lagrange
        self.corpos.append(corpo)

    def atualizar_todos(self):
        # Ordena os corpos pela posição no eixo x
        self.corpos.sort(
            key = lambda item: item.posicao[0]
        )
        for corpo in self.corpos:
            # Move e desenha cada corpo
            corpo.mover()
            corpo.desenhar()

    def desenhar_todos(self):
        # Define os limites dos eixos
        self.eixo.set_xlim(
            (-self.tamanho / 2, self.tamanho / 2)
        )
        self.eixo.set_ylim(
            (-self.tamanho / 2, self.tamanho / 2)
        )
        self.eixo.set_zlim(
            (-self.tamanho / 2, self.tamanho / 2)
        )

        # Remove os rótulos dos eixos
        self.eixo.xaxis.set_ticklabels([])
        self.eixo.yaxis.set_ticklabels([])
        self.eixo.zaxis.set_ticklabels([])

        # Pausa para atualizar a visualização e limpa o eixo
        matplotlib.pyplot.pause(0.05)
        self.eixo.clear()

    def calcular_interacoes_lagrangianas(self):
        # Calcula as interações gravitacionais entre os corpos
        for corpo in self.corpos:
            corpo.acelerar_devido_lagrange(self.corpos)

class CorpoLagrange:
    tamanho_minimo_exibicao = 1
    base_log_exibicao = 1.5

    def __init__(
        self,
        sistema_solar,
        massa,
        posicao = (0, 0, 0),
        velocidade = (0, 0, 0),
    ):
        # Inicializa um corpo no sistema Lagrange com massa, posição e velocidade
        self.sistema_solar = sistema_solar
        self.massa = massa
        self.posicao = np.array(posicao, dtype=float)
        self.velocidade = np.array(velocidade, dtype=float)
        self.tamanho_exibicao = max(
            math.log(self.massa, self.base_log_exibicao),
            self.tamanho_minimo_exibicao,
        )
        self.cor = "gray"
        self.sistema_solar.adicionar_corpo(self)

    def mover(self):
        # Atualiza a posição do corpo com base na sua velocidade
        self.posicao += self.velocidade

    def desenhar(self):
        # Desenha o corpo no eixo 3D
        self.sistema_solar.eixo.plot(
            *self.posicao,
            marker = "o",
            markersize = self.tamanho_exibicao + self.posicao[0] / 30,
            color = self.cor
        )

    def acelerar_devido_lagrange(self, corpos):
        # Calcula a aceleração devido à gravidade dos outros corpos
        forca_total = np.zeros(3)
        for outro in corpos:
            if outro is not self:
                distancia = outro.posicao - self.posicao
                magnitude_distancia = np.linalg.norm(distancia)
                magnitude_forca = self.massa * outro.massa / (magnitude_distancia ** 2)
                forca = (distancia / magnitude_distancia) * magnitude_forca
                forca_total += forca
        aceleracao = forca_total / self.massa
        self.velocidade += aceleracao

class Sol(CorpoLagrange):
    def __init__(
        self,
        sistema_solar,
        massa = 10_000,
        posicao = (0, 0, 0),
        velocidade = (0, 0, 0),
    ):
        # Inicializa o Sol com uma massa específica
        super(Sol, self).__init__(sistema_solar, massa, posicao, velocidade)
        self.cor = "yellow"

class Planeta(CorpoLagrange):
    cores = itertools.cycle([(1, 0, 0), (0, 1, 0), (0, 0, 1)])

    def __init__(
        self,
        sistema_solar,
        massa = 10,
        posicao = (0, 0, 0),
        velocidade = (0, 0, 0),
    ):
        # Inicializa um planeta com uma massa específica e cor cíclica
        super(Planeta, self).__init__(sistema_solar, massa, posicao, velocidade)
        self.cor = next(Planeta.cores)

class BuracoNegro(CorpoLagrange):
    def __init__(
        self,
        sistema_solar,
        massa = 10_000_000,
        posicao = (0, 0, 0),
        velocidade = (0, 0, 0),
    ):
        # Inicializa um buraco negro com uma massa específica
        super(BuracoNegro, self).__init__(sistema_solar, massa, posicao, velocidade)
        self.cor = "black"