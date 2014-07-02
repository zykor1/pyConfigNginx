# -*- coding: utf-8 -*-
from pide_informacion import solicita_string, solicita_int, solicita_si_no
from ejecuta_comando import ejecutar_comando, get_from_terminal, get_home
import os

class Configuracion:
	DIRECTORIO_INSTALAR = get_home() + "/server/nginx/"
	SUDO = False # No se ocupa
	FILENAME = "nginx-1.7.2.tar.gz"
	SUDO_ALL = False
	TEMP = ""

	# Configura el directorio a usar. Secuencia 2
	def configura_directorio(self):
		ejecutar_comando("clear")
		print "Por default nginx se instalara en: " + self.DIRECTORIO_INSTALAR
		if solicita_si_no("¿Deseas cambiar el directorio?\nrespuesta > "):
			self.DIRECTORIO_INSTALAR = solicita_string("¿Escribe la ruta absoluta donde lo deseas instalar. Ejemplo: /mi/ruta/ ?\nruta > ")
			if self.SUDO:
				self.configura_sudo_all("¿El nuevo directorio nesesita permisos superusuario?",
				 "1.- Si\n2.- No\nrespuesta > ")

	# Configura si se necesita usar sudo. Secuencia 1
	def configura_sudo(self):
		ejecutar_comando("clear")
		print "Usaras una terminal root o sudo para realizar la instalacion"
		if solicita_si_no("1.- SUDO \n2.- Terminal root \nrespuesta > "):
			self.SUDO = True

	# Configura si el sudo se tendra que usar en todas partes xD. No lleva una secuencia dentro del flujo
	def configura_sudo_all(self, mensaje, opciones):
		print mensaje
		if solicita_si_no(opciones):
			self.SUDO_ALL = True

	# Crea el directorio para instalar nginx. Secuencia 3
	def crea_directorio_nginx(self):
		if not os.path.isdir(self.DIRECTORIO_INSTALAR):
			comando = "mkdir -p " + self.DIRECTORIO_INSTALAR
			crea = ejecutar_comando(comando, self.SUDO_ALL)
			return crea
		return False

	# Crea el directorio temporal para descargar las cosas de nginx. Secuencia 4
	def crea_directorio_temporal(self):
		self.TEMP = self.DIRECTORIO_INSTALAR + "temp/"
		temp = self.TEMP + self.FILENAME
		if not os.path.exists(temp):
			comando = "mkdir " + self.TEMP
			crea = ejecutar_comando(comando, self.SUDO_ALL)
			return crea
		return False

	# Selecciona la version a elejir de nginx. Secuencia 5
	def version_nginx(self):
		ejecutar_comando("clear")
		print "Por default la version nginx que se instalara es: " + self.FILENAME
		if solicita_si_no("¿Deseas cambiar la version de nginx?\nrespuesta > "):
			self.DIRECTORIO_INSTALAR = solicita_string("¿Escribe la nueva version a descargar ejemplo: nginx-1.7.2.tar.gz ?\nversion > ")