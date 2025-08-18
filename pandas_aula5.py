# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

from google.colab import files
arquivo = files.upload()

#Criando o DataFrame
df = pd.read_excel("/content/drive/MyDrive/datasets/AdventureWorks.xlsx")

#vizualizando as 5 primeiras linhas 
df.head()

# Quantidade de linhas e colunas
df.shape

#Verificando os tipos de dados
df.dtypes

# Qual a Receita total
df["Valor Venda"].sum()

#Qual o custo total
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando coluna custo

df.head(1)

round(df["custo"].sum(), 2)
# round e o 2 ali no final é para arredondar pra 2 casas decimais

# Criar uma coluna de lucro que sera receita - custo
df["lucro"] = df["Valor Venda"] - df["custo"]

df.head(1)

# Agora sim lucro total
round(df["lucro"].sum(), 2)

#Criando coluna com total de dias para enviar o produto
df["Tempo Envio"] = df["Data Envio"] - df["Data Venda"]

df.head(1)

# media do tempo de envio de cada marca em dias
df["Tempo Envio"] = df["Tempo Envio"].dt.days

df["Tempo Envio"].dtype

df.head(1)

df.groupby("Marca")["Tempo Envio"].mean()

# verificando se existem valores ausentes
df.isnull().sum()

# Agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

pd.options.display.float_format = "{:20,.2f}".format

# Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

# Qual o total de podutos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total de Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head(1)

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="lucro x mes")
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal");

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="lucro x marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal")

df["Tempo Envio"].describe()

plt.boxplot(df["Tempo Envio"]);
# a bolinha é chamada de outline, outlier pode ser um ponto influente ou um valor inputado errado

plt.hist(df["Tempo Envio"]);

#tempo minimo de envio
df["Tempo Envio"].min()

#tempo maximo de envio
df["Tempo Envio"].max()

df[df["Tempo Envio"] == 20]

df.to_csv("df_vendas_novo.csv", index=False)