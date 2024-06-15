import os
import jsonpickle

def atualizar(idx, *args):
	obj = _from_args(*args)
	registros = buscar(type(obj))
	if not idx:
		idx = 0
		for c in registros.keys():
			try:
				if idx < (c := int(c)):
					idx = c
			except: pass
		idx += 1
	elif not (idx in registros):
		return False
	registros[idx] = obj
	salvar(type(obj), registros)
	return True

def inserir(*args):
	return atualizar(None, *args)

def buscar(tipo, cond=None):
	if not tipo:
		return {}
	elif type(tipo) == dict:
		registros = tipo
		return _filtrar(registros, cond)
	elif type(tipo) is str:
		arquivo = tipo
	else:
		arquivo = tipo.arquivo()
	
	if _criar(arquivo): 
		return {}
	with open(arquivo, 'r') as f:
		registros = jsonpickle.decode(f.read())
	return _filtrar(registros, cond)

def excluir(tipo, cond):
	registros = buscar(tipo)
	if callable(cond):
		novo = _filtrar(registros, cond, False)
		salvar(tipo, novo)
		return len(registros) - len(novo)
	elif cond in registros:
		del registros[cond]
		salvar(tipo, registros)
		return 1
	return 0

def salvar(tipo, registros):
	if (not tipo) or (not registros) or len(registros) == 0: 
		return
	elif type(tipo) is str:
		arquivo = tipo
	else:
		arquivo = tipo.arquivo()
	_criar(arquivo)
	with open(arquivo, 'w') as f:
		f.write(jsonpickle.encode(registros, indent=4))

def _from_args(*args):
	if len(args) == 1:
		return args[0]
	elif len(args) > 1:
		return args[0](*args[1:])
	raise TypeError(args)

def _filtrar(registros, cond, k=True):
	if cond == None:
		return registros or {}
	elif not callable(cond):
		cond = str(cond)
		if cond in registros:
			return { cond: registros[cond] }
		return {}
	k = not not k
	try:
		return { c: r 
			for c, r in registros.items()
				if k == (not not cond(c, r))
		}
	except TypeError:
		return { c: r
			for c, r in registros.items()
				if k == (not not cond(r))
		}

def _criar(arquivo):
	if not os.path.exists(arquivo):
		with open(arquivo, 'w') as f:
			f.write(jsonpickle.encode({}))
			return True
	return False