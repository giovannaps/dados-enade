import pandas as pd 
import matplotlib.pyplot as plt


#Lendo o arquivo excel
dadosPlanilha = pd.read_excel('dadosenade.xlsx')

#Declarando as colunas e linhas
colunas = dadosPlanilha.columns     
linhas = dadosPlanilha.index

#Colocando dados principais dos gráficos como variáveis globais
x = dadosPlanilha['ANO']
y = dadosPlanilha['CONCEITO']

def dadosAno_Conceito(x,y):
	x = dadosPlanilha['ANO']
	y = dadosPlanilha['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='pink')
	plt.show()
	
def dadosUFPE(x, y):
	ufpe = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFPE"]
	x = ufpe['ANO']
	y = ufpe['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFPE)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show()  

def dadosFAINOR(x, y):
	fainor = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "FAINOR"]
	x = fainor['ANO']
	y = fainor['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (FAINOR)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 

def dadosUFBA(x, y):
	ufba = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFBA"]
	x = ufba['ANO']
	y = ufba['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFBA)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 

def dadosUNIFACS(x, y):
	unifacs = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UNIFACS"]
	x = unifacs['ANO']
	y = unifacs['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UNIFACS)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 

def dadosUEMA(x, y):
	uema = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UEMA"]
	x = uema['ANO']
	y = uema['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UEMA)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 

def dadosUFBA(x, y):
	ufba = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFBA"]
	x = ufba['ANO']
	y = ufba['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFBA)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 

	
def dadosIFCE(x, y):
	ifce = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "IFCE"]
	x = ifce['ANO']
	y = ifce['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (IFCE)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 

def dadosUFC(x, y):
	ufc = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFC"]
	x = ufc['ANO']
	y = ufc['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFC)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 

def dadosUNIFOR(x, y):
	unifor = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UNIFOR"]
	x = unifor['ANO']
	y = unifor['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UNIFOR)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 

def dadosUFRN(x, y):
	ufrn = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UFRN"]
	x = ufrn['ANO']
	y = ufrn['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UFRN)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 

def dadosUNP(x, y):
	unp = dadosPlanilha[dadosPlanilha['UNIVERSIDADE'] == "UNP"]
	x = unp['ANO']
	y = unp['CONCEITO']
	plt.title("Gráfico de Barras - Ano x Conceito (UNP)")
	plt.xlabel("Ano")
	plt.ylabel("Conceito")
	plt.bar(x, y, color='blue')
	plt.show() 
	
	

def dadosGraficos():
	dadosUFPE(x,y)
	dadosFAINOR(x,y)
	dadosUFBA(x,y)
	dadosUNIFACS(x,y)
	dadosUEMA(x,y)
	dadosIFCE(x,y)
	dadosUFC(x,y)
	dadosUNIFOR(x,y)
	dadosUFRN(x,y)
	dadosUNP(x,y)
	plt.show()

dadosGraficos()

#dadosUFPE(x,y)
#dadosAno_Conceito(x,y)



#mudar função para uma q mostre todas as universidades em um unico grafico



#preciso usar o plt.show() para mostrar o grafico
#plt.bar() cria o grafico de barras