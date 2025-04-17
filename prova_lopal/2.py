# (20) Crie uma função chamada alerta_uso que recebe como parâmetro uma lista com os valores de uso de CPU de uma região. A função deve retornar True se algum valor ultrapassar 85% de uso, e False caso contrário. Teste a função para todas as regiões da matriz.

uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

def alerta_uso(uso_cpu):
  for i in range(len(uso_cpu)):

    parametro = 85

    for _ in uso_cpu[i]:
      
      print()
      if _ >= parametro:
        verificar = True
        print(f"Região {i}, {verificar} {_}%")
      else:
        verificar = False
        print(f"Região {i}, {verificar} {_}%")

alerta_uso(uso_cpu)

