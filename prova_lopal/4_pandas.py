# (20) Utilizando a biblioteca pandas, crie um DataFrame com os dados da matriz acima. Os nomes das linhas devem ser ["hora_1", "hora_2",..., "hora_10"] e as colunas representam as regiões ["us-east-1", "us-west-2", "eu-central-1", "sa-east-1", " ap-southeast-1"  ].  

import pandas as pd

uso_cpu = [
[20, 25, 40, 50, 45],
[30, 35, 50, 60, 40],
[15, 20, 30, 25, 35],
[10, 15, 25, 35, 45],
[10, 15, 25, 35, 45],
[10, 15, 25, 35, 45],
[10, 15, 25, 35, 45],
[10, 15, 25, 35, 45],
[10, 15, 25, 35, 45],
[10, 15, 25, 35, 45],
]

linhas = ["hora_1", "hora_2","hora_3", "hora_4","hora_5",
           "hora_6","hora_7", "hora_8","hora_9", "hora_10"]

colunas = ["us-east-1", "us-west-2", "eu-central-1", "sa-east-1", " ap-southeast-1" ]

df = pd.DataFrame(uso_cpu, index=linhas, columns=colunas)

print(df)