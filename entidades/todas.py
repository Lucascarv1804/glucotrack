from .padrao import Entidade
from util.dados import *

class Glicemia(Entidade):
	# arquivo = 'dados/glicemia.json'
	attr = [
		"paciente",
		"data",
		"valor",
	]
	form = [
		"Data e hora da afericao [dd/mes/yy hh:min] ", checar_dh,
		"Valor registrado: ", float,
	]

class Medicacao(Entidade):
	# arquivo = 'dados/medicacao.json'
	attr = [
		"paciente",
		"nome",
		"dosagem",
		"hora_inicial",
		"intervalo",
		"lembrar",
	]
	form = [
		"Nome da medicacao: ", str,
		"Dose prescrita: ", str,
		"Horario diario inicial: ", checar_hora,
		"Intervalo: ", is_type(int), 
		"Alarmar? (S/N) ", checar_sn,
	]

class Paciente(Entidade):
	# arquivo = 'dados/paciente.json'
	attr = [
		"nome", 
		"idade", 
		"sexo", 
		"peso", 
		"altura",
	]
	form = [
		"Nome: ", str,
		"Idade: ", int,
		"Sexo (F/M) ", checar_sexo,
		"Peso (kg) ", float,
		"Altura (cm) ", int,
	]
	def primeiro_nome(self):
		return self.nome.split(' ', 1)[0]

class Refeicao(Entidade):
	# arquivo = 'dados/refeicao.json'
	attr = [
		"paciente",
		"nome",
		"data",
		"proteinas",
		"gorduras",
		"carboidratos",
	]
	form = [
		"Nome do alimento: ", str,
		"Data e hora da ingestao [dd/mes/yy hh:min] ", checar_dh,
		"Proteínas (g) ", float,
		"Gorduras (g) ", float,
		"Carboidratos (g) ", float,
	]
	def calorias(self):
		return ( 0
			+ self.carboidratos * 4
			+ self.proteinas * 4
			+ self.gorduras * 9)



