# (20) Crie uma função chamada dados_crescente que recebe como parâmetro uma lista com os valores de uso de CPU de uma região. A função deve retornar a lista organizada em ordem crescente, do menor uso de CPU para o maior. Teste a função para todas as regiões da matriz

uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]


def dados_crescente():
    for i in range(len(uso_cpu)):

        uso_cpu[i].sort()

        print()
        print(f"ordem das linhas {i}")
        print(uso_cpu[i])

dados_crescente()