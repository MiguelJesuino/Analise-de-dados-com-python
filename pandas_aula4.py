# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib as plt

df1 = pd.read_excel("/content/drive/MyDrive/datasets/Aracaju.xlsx")
df2 = pd.read_excel("/content/drive/MyDrive/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("/content/drive/MyDrive/datasets/Natal.xlsx")
df4 = pd.read_excel("/content/drive/MyDrive/datasets/Recife.xlsx")
df5 = pd.read_excel("/content/drive/MyDrive/datasets/Salvador.xlsx")

df = pd.concat([df1, df2, df3, df4, df5])

# faz uma contagem
df["LojaID"].value_counts(ascending=False)

df["LojaID"].value_counts(ascending=False).plot.bar()

"""df["LojaID"].value_counts(ascending=False).plot.barh()"""

df["LojaID"].value_counts(ascending=False).plot.barh();

df["Receita"] = df["Vendas"].mul(df["Qtde"])

df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

#Total vendas por cidade
df["Cidade"].value_counts()

# Adicionando um titulo e alterando nome dos eixos
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title="Total de vendas por Cidade");
plt.xlabel("Cidade");
plt.ylabel("Total Vendas");

# mudando Cor  
df["Cidade"].value_counts().plot.bar(title="Total de vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

# Alterando estilo
plt.style.use("ggplot")

df["Data"] = df["Data"].view("int64")

df.dtypes

df["Data"] = pd.to_datetime(df["Data"])

df.dtypes

df["Ano_venda"] = df["Data"].dt.year

# criando colunas mes_venda e dia_venda
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

#Criando a coluna de trimestre
df["Trimestre_venda"] = df["Data"].dt.quarter

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title="Total de Produtos Vendidos Por Mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()





df.groupby(df["mes_venda"])["Qtde"].sum()

df_2019 = df[df["Ano_venda"] == 2019]

df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(color="orange", marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total Proidutos Vendidos")
plt.legend();

#hisograma
plt.hist(df["Qtde"], color="black")

df_2019["Receita"] = df_2019["Vendas"].mul(df_2019["Qtde"])

df_2019.columns

# grafico de pontinho
plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"], color="Black");

df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(color="Black", marker = "o")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.savefig("Grafico QTDE x MES.png")