import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo excel
dadosPlanilha = pd.read_excel('dadosenade.xlsx')

# Declarando as colunas e linhas
colunas = dadosPlanilha.columns
linhas = dadosPlanilha.index


# Configurando o estilo dos gráficos
plt.rcParams['font.serif'] = ['DejaVu Sans']
plt.rcParams['font.size'] = 12

# Mostrar o gráfico de todas as universidades
def dadosGraficos():
    for i in dadosPlanilha['UNIVERSIDADE'].unique():
        universidade = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == i]
        x = universidade['ANO'].astype(str)
        y = universidade['CONCEITO']

        plt.ylim(0, 5)
        plt.bar(x, y, color='#5177E6')
        plt.title(i, fontweight='bold')
        plt.xlabel("Ano")
        plt.ylabel("Conceito")
        plt.show()

  
#Comparar universidades em 2026
def compararUniversidades():
    ano = dadosPlanilha[dadosPlanilha['ANO'] == 2026]
    x = ano['UNIVERSIDADE']
    y = ano['CONCEITO']

    plt.title("Comparação de Conceitos das Universidades", fontweight='bold')
    plt.xlabel("Universidade")
    plt.ylabel("Conceito")
    plt.ylim(0, 5)
    plt.bar(x, y, color='#5177E6')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.show()

# Exibir função com todos os gráficos
dadosGraficos()

# Exibir função com comparação entre universidades em 2026
compararUniversidades()












