from ejecuta_comando import ejecutar_comando, get_from_terminal, get_home
from configuracion_nginx import Configuracion


class Instalacion:
	conf = Configuracion()
	dir_temp = self.conf.DIRECTORIO_INSTALAR + "temp/" + self.conf.FILENAME
	def __init__(self):
		self.conf.configura_sudo()
		self.conf.configura_directorio()
		self.conf.crea_directorio_nginx()
		self.conf.crea_directorio_temporal()
		self.conf.version_nginx()


	def descargar_nginx():
		comando = "wget http://nginx.org/download/" + self.conf.FILENAME
		return ejecutar_comando(comando, self.conf.SUDO_ALL)


	def descomprimir_nginx():
		comando = "tar -xzf " + self.conf.TEMP + self.conf.FILENAME
		return ejecutar_comando(comando, self.conf.SUDO_ALL)

	def primer_paso_instalacion():


#call(["wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'"], shell = True)

#call([" /home/zykor/"], shell = True)
#call(["pwd"], shell = True)


# wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'
# tar -xzf nginx-1.7.2.tar.gz
# cd nginx-1.7.2
# ./configure
# make
# sudo make install