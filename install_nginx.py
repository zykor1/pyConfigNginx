# -*- coding: utf-8 -*-
from pide_informacion import solicita_string, solicita_int, solicita_si_no
from ejecuta_comando import ejecutar_comando, get_from_terminal, get_home

class Configuracion:
	DIRECTORIO_INSTALAR = get_home() + "/server/nginx/"
	SUDO = False # No se ocupa

	def configura_directorio(self):
		print "Por default nginx se instalara en: " + self.DIRECTORIO_INSTALAR
		if solicita_si_no("¿Deseas cambiar el directorio?\nrespuesta > "):
			self.DIRECTORIO_INSTALAR = solicita_string("¿Escribe la ruta absoluta donde lo deseas instalar?\nruta > ")

	def configura_sudo(self):
		print "Usaras una terminal root o sudo para realizar la instalacion"
		if solicita_si_no("1.- Terminal root \n2.- Sudo\nrespuesta > "):
			self.SUDO = True


conf = Configuracion()
conf.configura_directorio()
conf.configura_sudo()
print conf.DIRECTORIO_INSTALAR
print conf.SUDO

#call(["wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'"], shell = True)

#call([" /home/zykor/"], shell = True)
#call(["pwd"], shell = True)


# wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'
# tar -xzf nginx-1.7.2.tar.gz
# cd nginx-1.7.2
# ./configure
# make
# sudo make install