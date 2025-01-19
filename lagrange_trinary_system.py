# lagrange_trinary_system.py

from lagrange import SistemaLagrange, Sol, Planeta

sistema = SistemaLagrange(tamanho=256)

sois = (
    Sol(sistema, posicao=(60, 60, 60), velocidade=(6, 0, 6)),
    Sol(sistema, posicao=(-60, -60, 60), velocidade=(-6, 0, -6)),
    Sol(sistema, posicao=(10, 10, -60), velocidade=(0, 6, -6)),
)

planetas = (
    Planeta(
        sistema,
        15,
        posicao=(110, 110, 10),
        velocidade=(1, 6, 6),
    ),
    Planeta(
        sistema,
        25,
        posicao=(10, 10, 10),
        velocidade=(-11, 11, 1),
    ),
)

while True:
    sistema.calcular_interacoes_lagrangianas()
    sistema.atualizar_todos()
    sistema.desenhar_todos()