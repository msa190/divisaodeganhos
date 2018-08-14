#encoding: utf-8
import os
entradao = open('entrada.txt', 'r')
entradai = open('entrada.txt','a')
divisao1 = open('divisao.txt', 'r')
divisao = []
razao = []
for i in divisao1:
	divisao.append(i.split(';')[0])
	razao.append((i.split(';')[1]))
def ganho():
	nome = raw_input('Qual o nome para o ganho? ')
	valor = raw_input('Quanto ganhou? ')
	dia = input('Que dia?(dois digitos) ')
	mes = input('Quem mes?(dois digitos) ')
	ano = input('Em que ano?(quatro digitos) ')
	string = str(nome) + ';' + str(valor) + ';' + str(dia)+';' +str(mes)+ ';' + str(ano)+';'+'\n'
	entradai.write(string)
	for i, j in enumerate(divisao[1:]):
		carteira = open(j,'a')
		carteira.write(str(nome) + ';' + str(float(valor)*float(razao[i+1])) + ';' + str(dia)+';' +str(mes)+ ';' + str(ano)+';'+'\n')
	print string
	
def registro(ano,mes):
	for i in entradao:
		anox = i.split(';')[4]
		mesx = i.split(';')[3]
		string = i.split(';')[0] +'   '+ i.split(';')[1] +'   '+ i.split(';')[2] +'   '+ i.split(';')[3]+'   '+ i.split(';')[4]
		if str(anox) == str(ano) and str(mesx) == str(mes):
			print string
def verifica_razao(razao1):
	soma = 0
	for i in razao[1:]:
		i = float(i)
		soma = soma + i
	if soma+razao1 < 1:
		print 'Atenção, seu dinheiro não está todo dividido'
		return 1
	if soma + razao1 >1:
		if soma > 1:
			print 'Erro ao cadastrar divisao: Seu dinheiro está todo dividido, exclua alguma carteira'
			return 0
		else:
			print 'Erro ao cadastrar divisao: Escolha outra razão, restam apenas ' + str(1-soma)
			return 0
def cadastro_carteira(nome, razao):
	divisaoin = open('divisao.txt','a')
	if verifica_razao(razao) == 1:
		divisaoin.write(nome+'.txt'+';'+str(razao)+';'+'\n')
	else:
		pass
class Usuario():
	def __init__(self, nome='', idade=0):
		self.nome = nome
		self.idade = idade
	def setNome(self,nome):
		self.nome = nome
	def setIdade(self,idade):
		self.idade = idade
	def takeRatio(self):
		pass#assumir um conjunto de carteiras e razões
class Carteira():
	def __init__(self, nome='a', razao = 0, saldo = 0):
		self.nome = nome
		self.razao = razao
		self.saldo = saldo
		entrada = open(self.nome+'.txt', 'a')
	def gasto(self, valor=0, nome = '', dia = '', mes = '', ano = ''):
		entrada.write(nome+';'+str(-valor)+str(dia)+str(mes)+str(ano))
	
	def ganho(self, valor=0, nome = '', dia = '', mes = '', ano = ''):
		entrada.write(nome+';'+str(valor)+str(dia)+str(mes)+str(ano))
	entradas = []
	for linha in entrada:
		entradas.append(linha)
	for linha in entradas[1:]:
		self.saldo = self.saldo + float(linha.split(';')[1])
		
#viagem = Carteira('viagem',0.1,200)
