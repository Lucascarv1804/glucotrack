from entidades.todas import *
from crud.io import *


def tela_login():
	def entrar():
		pacientes = listar(Paciente, None)
		if (not pacientes) or len(pacientes) == 0:
			print_wait("Favor cadastrar um usuario para comecar.")
			return
		idx = perguntar(
			"Codigo de usuario: ", 
			lambda k: k if k in pacientes else None, None,
			"Codigo invalido",
		)
		welcome(pacientes[idx])
		tela_principal(idx)
		
	tela_base("Login", [
		"Entrar", entrar,
		"Cadastrar usuário",
		lambda: perguntar_inserir(Paciente, None),
		"Excluir",
		lambda: perguntar_excluir(Paciente, None),
	])


def tela_principal(id_pct):
	tela_base("Home", [
		"Cadastro", 
		lambda: perguntar_atualizar(Paciente, id_pct),
		"Medicacao", 
		lambda: tela_crud(Medicacao, id_pct),
		"Glicemia", 
		lambda: tela_crud(Glicemia, id_pct),
		"Refeicao", 
		lambda: tela_crud(Refeicao, id_pct),
	])
	