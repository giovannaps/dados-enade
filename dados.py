import pandas as pd 
import matplotlib.pyplot as plt


#Lendo o arquivo excel
dadosPlanilha = pd.read_excel('dadosenade.xlsx')

#Declarando as colunas e linhas
colunas = dadosPlanilha.columns     
linhas = dadosPlanilha.index

#Colocando dados principais dos gráficos como variáveis globais
x = dadosPlanilha['ANO'].astype(str)
y = dadosPlanilha['CONCEITO'].astype(str)

#configurando o estilo dos gráficos
plt.rcParams['font.serif'] = ['DejaVu Sans']
plt.rcParams['font.size'] = 12


#declarando gráficos para cada universidade 
def dadosUFPE(x, y):
	ufpe = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFPE"]
	x = ufpe['ANO'].astype(str)
	y = ufpe['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFPE)",
	fontweight='bold' )
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show()  

def dadosFAINOR(x, y):
	fainor = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "FAINOR"]
	x = fainor['ANO'].astype(str)
	y = fainor['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (FAINOR)",
    fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 

def dadosUFBA(x, y):
	ufba = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFBA"]
	x = ufba['ANO'].astype(str)
	y = ufba['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFBA)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 

def dadosUNIFACS(x, y):
	unifacs = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UNIFACS"]
	x = unifacs['ANO'].astype(str)
	y = unifacs['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UNIFACS)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 

def dadosUEMA(x, y):
	uema = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UEMA"]
	x = uema['ANO'].astype(str)
	y = uema['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UEMA)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 

def dadosUFBA(x, y):
	ufba = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFBA"]
	x = ufba['ANO'].astype(str)
	y = ufba['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFBA)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 

	
def dadosIFCE(x, y):
	ifce = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "IFCE"]
	x = ifce['ANO'].astype(str)
	y = ifce['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (IFCE)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 

def dadosUFCFortaleza(x, y):
	ufc = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFC"]
	ufc = dadosPlanilha[dadosPlanilha['CAMPUS'] == "Fortaleza"]
	x = ufc['ANO'].astype(str)
	y = ufc['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFC FORTALEZA)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 

def dadosUFCSobral(x, y):
	ufc = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFC"]
	ufc = dadosPlanilha[dadosPlanilha['CAMPUS'] == "Sobral"]
	x = ufc['ANO'].astype(str)
	y = ufc['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFC SOBRAL)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 


def dadosUNIFOR(x, y):
	unifor = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UNIFOR"]
	x = unifor['ANO'].astype(str)
	y = unifor['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UNIFOR)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 

def dadosUFRN(x, y):
	ufrn = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFRN"]
	x = ufrn['ANO'].astype(str)
	y = ufrn['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFRN)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 

def dadosUNP(x, y):
	unp = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UNP"]
	x = unp['ANO'].astype(str)
	y = unp['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UNP)",
	fontweight='bold')
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.ylim(0,5)
	plt.bar(x, y, color='#5177E6')
	plt.show() 
	
	
#mostrar o gráfico de todas as universidades
def dadosGraficos():
	plt.ylim(0, 5)
	dadosUFPE(x,y)
	dadosFAINOR(x,y)
	dadosUFBA(x,y)
	dadosUNIFACS(x,y)
	dadosUEMA(x,y)
	dadosIFCE(x,y)
	dadosUFCFortaleza(x,y)
	dadosUFCSobral(x,y)
	dadosUNIFOR(x,y)
	dadosUFRN(x,y)
	dadosUNP(x,y)
	plt.show()

#exibir função com todos os gráficos 
dadosGraficos()











