# lagrange_binary_system.py

from lagrange import SistemaLagrange, Sol, Planeta

sistema = SistemaLagrange(256)

sois = (
    Sol(sistema, posicao=(50, 50, 50), velocidade=(5, 0, 5)),
    Sol(sistema, posicao=(-50, -50, 50), velocidade=(-5, 0, -5)),
)

planetas = (
    Planeta(
        sistema,
        10,
        posicao=(100, 100, 0),
        velocidade=(0, 5, 5),
    ),
    Planeta(
        sistema,
        20,
        posicao=(0, 0, 0),
        velocidade=(-10, 10, 0),
    ),
)

while True:
    sistema.calcular_interacoes_lagrangianas()
    sistema.atualizar_todos()
    sistema.desenhar_todos()