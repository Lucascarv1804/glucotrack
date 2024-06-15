from prettytable import PrettyTable
import pyfiglet
import os
from util.dados import *
from .crud import *

CANCELADO = "Operacao cancelada."
CONCLUIDO = "Operacao concluida."
PERDIDO = "Não encontrado."
INVALIDO = "Entrada invalida!"

WELCOME = None
def welcome(paciente):
	nome = paciente.primeiro_nome().upper()
	w = PrettyTable()
	w.header = False
	w.add_row([f"Ola, {nome}"])
	global WELCOME
	WELCOME = w

def limpa_tela():
	os.system("cls" if os.name == "nt" else "clear")
	
def nome_sistema():
	titulo = pyfiglet.figlet_format("GlucoTrack", font='doom')
	print(titulo, flush=True)

def tela_crud(tipo, id_pct):
	tela_base(tipo.classname(True), [
		"Registrar", 
		lambda: perguntar_inserir(tipo, id_pct),
		"Listar", 
		lambda: listar(tipo, por_paciente(id_pct)),
		"Editar", 
		lambda: perguntar_atualizar(tipo, id_pct),
		"Remover",
		lambda: perguntar_excluir(tipo, id_pct),
	])

def tela_base(titulo, opcoes):
	acoes = opcoes[1::2]
	opcoes = opcoes[0::2]

	def checar(u):
		u = int(u) - 1
		if u == -1:
			return 0
		elif 0 <= u < len(opcoes):
			return acoes[u]
		return None

	operacoes = PrettyTable()
	operacoes.field_names = ["#", str(titulo).upper()]
	for i, op in enumerate(opcoes):
		operacoes.add_row([f"{i+1}", f"{op}"])
	operacoes.add_row(["0", "Sair"])

	while True:
		limpa_tela()
		nome_sistema()
		print(WELCOME) if WELCOME else None 
		print(operacoes)
		choice = perguntar("Digite a desejada: ", checar, 
			None, INVALIDO)
		if choice == 0:
			return
		choice()
		print_wait()

def perguntar(msg, checar=None, padrao=None, err=None):
	if type(checar) is list:
		opcoes = checar
		checar = lambda x: x if x in opcoes else None
	elif not callable(checar):
		checar = lambda x: x

	if err and not callable(err):
		_err = err
		err = lambda: print(_err)

	while True:
		resp = input(msg)
		if resp != "": 
			try:
				resp = checar(resp)
				if resp != None:
					return resp
				else: err()
			except Exception as e:
				_ = err() if err else print(e)
		elif padrao != None:
			return padrao

def perguntar_tipo(tipo, empty=None) -> dict:
	form = tipo.form[0::2]
	check = tipo.form[1::2]
	attr = tipo.atributos()[-len(form):]
	triple = lambda a, b, c: (a, b, c)
	reg = {}
	for k, msg, ch in map(triple, attr, form, check):
		reg[k] = perguntar(msg, ch, 
			empty and getattr(empty, k))
	return reg

def perguntar_inserir(tipo, id_pct):
	reg = perguntar_tipo(tipo)
	if id_pct != None:
		reg['paciente'] = id_pct
	return inserir(tipo(reg))

def perguntar_atualizar(tipo, id_pct):
    if 'paciente' in tipo.atributos():
        registros = listar(tipo, por_paciente(id_pct))
    else:
        registros = listar(tipo, id_pct)

    if len(registros) == 0:
        return None
    elif len(registros) == 1:
        if not perguntar("Deseja alterar? (S/N) ", checar_sn):
            return None
        idx = next(iter(registros.keys()))
    elif len(registros) > 1:
        idx = perguntar("ID a editar: ", is_type(int), 
            False, INVALIDO)
        if not idx:
            print(CANCELADO)
            return None
    idx = str(idx)
    reg = buscar(registros, idx)
    if len(reg) > 0:
        reg = perguntar_tipo(tipo, reg[idx])

        if 'paciente' in tipo.atributos():
            reg['paciente'] = id_pct
        reg = tipo(reg)
        print(reg.table())
        if atualizar(idx, reg):  # Passar o registro atualizado
            print(CONCLUIDO)
            return reg
    print(PERDIDO)
    return None


def perguntar_excluir(tipo, id_pct):
	registros = listar(tipo, por_paciente(id_pct))
	idx = perguntar("ID a excluir: ", 
		lambda x: str(int(x)), False, INVALIDO)
	if not idx:
		return print(CANCELADO)
	elif excluir(tipo, idx):
		return print(CONCLUIDO)
	return print(PERDIDO)

def listar(tipo, cond=None):
	tabela = PrettyTable()
	registros = buscar(tipo, cond)
	if len(registros) == 0:
		tabela.header = False
		tabela.add_row(["Sem registros!"])
		print(tabela)
		print()
		return {}
	attr = tipo.atributos()
	tabela.field_names = ['#', *attr]
	for c, r in registros.items():
		tabela.add_row(r.row(c))
	print(tabela)
	return registros

def print_wait():
	input("Pressione Enter para continuar...")

def por_paciente(pct):
	if pct == None: return None
	return lambda c, r: r.paciente == pct

