# -*- coding: utf-8 -*-

import pandas as pd

# Arquivos
df1 = pd.read_excel("/content/drive/MyDrive/datasets/Aracaju.xlsx")
df2 = pd.read_excel("/content/drive/MyDrive/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("/content/drive/MyDrive/datasets/Natal.xlsx")
df4 = pd.read_excel("/content/drive/MyDrive/datasets/Recife.xlsx")
df5 = pd.read_excel("/content/drive/MyDrive/datasets/Salvador.xlsx")

# mostra as 5 primeiras linhas, a "cabeça" do arquivo
df1.head()

#Junta os arquivos em um só
df = pd.concat([df1,df2,df3,df4,df5])

df.sample(5)

# verificando o tipo do dado
df.dtypes

# mudando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")

df.dtypes

# df.é nulo?".isnull" se sim some ".sum()"
df.isnull().sum()

# Substituindo valores nulos pela media da coluna vendas
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

df.isnull().sum()

# substituindo valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

# Apagando as linhas com valores nulos
df.dropna(inplace=True)

# Apagando as linhas com valores nulos com base somente eu uma coluna
df.dropna(subset=["Vendas"], inplace=True)

# Criando coluna de receita
# receita é igual a vendas multiplicado por quantidade
df["Receita"] = df["Vendas"].mul(df["Qtde"])

df.head()

"""quantidade pode ser achada dividindo a receita por Vendas """

# vendo qual foi a maior receita
df["Receita"].max()

df["Receita"].min()

# TOP 3 maiores receitas nlargest
df.nlargest(3,"Receita")

# TOP 3 menores Receitas
df.nsmallest(3, "Receita")

# Agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()

# Ordenando o conjunto de dados
df.sort_values("Receita", ascending=False).head(10)