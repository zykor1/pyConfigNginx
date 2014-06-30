from subprocess import call, Popen, PIPE

def get_home():
	auxHome = Popen("echo $HOME", shell=True, stdout=PIPE,  stderr=PIPE)
	home =   auxHome.communicate()
	home = home[0].rstrip()
	return home

def get_from_terminal(comando):
	"""
		Obtiene la informacion regresada por el terminal, retorna lo mismo que la terminal
	"""
	auxRes = Popen(comando, shell=True, stdout=PIPE,  stderr=PIPE)
	res = auxRes.communicate()
	return res[0].rstrip

def ejecutar_comando(comando):
	"""
		Ejecuta un comando en la terminal y regresa 1 True, 0 False
	"""
	res = call([comando], shell = True)
	return res