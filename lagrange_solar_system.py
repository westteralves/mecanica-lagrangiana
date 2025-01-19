# lagrange_solar_system.py

from lagrange import SistemaLagrange, Sol, Planeta

sistema = SistemaLagrange(tamanho=256)

sol = Sol(sistema, posicao=(0, 0, 0), velocidade=(0, 0, 0))

planetas = (
    Planeta(sistema, massa=12, posicao=(90, 40, 0), velocidade=(3, 3, 7)),
    Planeta(sistema, massa=24, posicao=(150, 60, 0), velocidade=(1, 1, 4)),
    Planeta(sistema, massa=90, posicao=(220, 80, 0), velocidade=(1.2,  0.8, 2.5))
)

while True:
    sistema.calcular_interacoes_lagrangianas()
    sistema.atualizar_todos()
    sistema.desenhar_todos()