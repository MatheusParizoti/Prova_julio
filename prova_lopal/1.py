## (20) Cosiderando a matriz abaixo, crie um laço for para calcular a média de uso de CPU por linha e ## imprima os resultados com 2 casas decimais. 

uso_cpu = [
[80, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 92, 25, 35, 90, 45, 50, 55, 60],
[10, 15, 25, 35, 145, 50, 55, 60, 65, 85],
[90, 25, 205, 35, 145, 50, 55, 60, 65, 85]
]



for i in range(len(uso_cpu)):
    linha = sum(uso_cpu[i])
    media = linha / len(uso_cpu[i])
    print()
    print(f"media linha {i}")
    print(media)


