# -*- coding: utf-8 -*-


import pandas as pd

df1 = pd.read_excel("/content/drive/MyDrive/datasets/Aracaju.xlsx")
df2 = pd.read_excel("/content/drive/MyDrive/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("/content/drive/MyDrive/datasets/Natal.xlsx")
df4 = pd.read_excel("/content/drive/MyDrive/datasets/Recife.xlsx")
df5 = pd.read_excel("/content/drive/MyDrive/datasets/Salvador.xlsx")

df = pd.concat([df1,df2,df3,df4,df5])

df["Receita"] = df["Vendas"].mul(df["Qtde"])

"""# DATA

"""

# Transformando a coluna de data en tipo inteiro
df["Data"] = df["Data"].view("int64")

df["Data"].dtype

# transformando a coluna data em data
df["Data"] = pd.to_datetime(df["Data"])

# Verificando tipos de dados
df.dtypes

# Agrupamento por ano
# vai na data e retorna só o ano dt.year
df.groupby(df["Data"].dt.year)["Receita"].sum()

# Criando ua nova coluna com o ano
df["Ano_venda"] = df["Data"].dt.year

# Criando colunas mes_venda e dia_venda
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

df.sample(5)

# Retorna data mais antiga
df["Data"].min()

# Calculando diferença de dias
df['diferenca_dias'] = df["Data"] - df["Data"].min()

df.sample(5)

#Criando a coluna de trimestre
df["Trimestre_venda"] = df["Data"].dt.quarter

# Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

vendas_marco_19.sample(3)

