import re
import time
from datetime import datetime

formato_data = "%d/%m/%y"
formato_hora = "%H:%M"

descricao_sexo = {
	"F": "Feminino",
	"f": "Feminino",
	"M": "Masculino",
	"m": "Masculino",
}

def is_type(tipo):
	return lambda x: str(tipo(x))

def checar_sexo(x):
	if x in descricao_sexo:
		return x.upper()
	return None

def checar_email(email):
	padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
	if re.match(padrao, email):
		return email
	return None

def checar_hora(u):
	return time.strptime(u, formato_hora) and u

def checar_dh(u):
	f = f"{formato_data} {formato_hora}"
	return datetime.strptime(u, f) and u
	
def checar_sn(x):
	if x in ['S', 'N', 's', 'n']:
		return x.upper() == 'S'
	return None