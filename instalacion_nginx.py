# -*- coding: utf-8 -*-
from ejecuta_comando import ejecutar_comando, get_from_terminal, get_home
from pre_configuracion_nginx import Configuracion
import io, json


class Instalacion:
	conf = Configuracion()
	ruta_nginx = ""
	def __init__(self):
		self.conf.configura_sudo()
		self.conf.configura_directorio()
		self.conf.crea_directorio_nginx()
		self.conf.crea_directorio_temporal()
		self.conf.version_nginx()


	def descargar_nginx(self):
		print "Descargando"
		comando = self.conf.TEMP +  " wget http://nginx.org/download/" + self.conf.FILENAME
		return ejecutar_comando(comando, self.conf.SUDO_ALL)


	def descomprimir_nginx(self):
		print "Descomprimiendo"
		comando = "tar -xzf " + self.conf.TEMP + self.conf.FILENAME
		return ejecutar_comando(comando, self.conf.SUDO_ALL)

	def primer_paso_instalacion(self):
		print "Instalando: ./configure"
		extension = ".tar.gz"
		if ".zip" in self.conf.FILENAME:
			extension = ".zip"
		ruta_nginx = self.conf.TEMP + self.conf.FILENAME.split(extension)[0] + "/" 
		if ejecutar_comando(ruta_nginx + "configure", self.conf.SUDO_ALL) == 1:
			self.segundo_paso_instalacion(ruta_nginx)
		return False


	def segundo_paso_instalacion(self, ruta_nginx):
		print "Instalando: make"
		res = ejecutar_comando(ruta_nginx + "make" + self.conf.SUDO_ALL)
		if res == 1:
			self.tercer_paso_instalacion(ruta_nginx)
		return False


	def tercer_paso_instalacion(self, ruta_nginx):
		print "Instalando: make install"
		return ejecutar_comando(ruta_nginx + "make install", self.conf.SUDO_ALL)


	def genera_configure(self):
		auxConfigure = (
			"./configure   --prefix={prefix}  "
			"--sbin-path={sbin_path}  "
			"--conf-path={conf_path}  "
			"--error-log-path={error_log_path}  "
			"--http-log-path={http_log_path}  "
			"--pid-path={pid_path}  "
			"--lock-path={lock_path}  "
			"--http-client-body-temp-path={http_client_body_temp_path}  "
			"--http-proxy-temp-path={http_proxy_temp_path}  "
			"--http-fastcgi-temp-path={http_fastcgi_temp_path}  "
			"--with-http_flv_module  "
			"--with-http_ssl_module  "
			"--with-http_gzip_static_module"
		)
		return auxConfigure.format(
			prefix=self.conf.DIRECTORIO_INSTALAR,
			sbin_path=self.conf.DIRECTORIO_INSTALAR + "sbin/nginx",
			conf_path=self.conf.DIRECTORIO_INSTALAR + "etc/nginx.conf",
			error_log_path=self.conf.DIRECTORIO_INSTALAR + "/logs/error.log",
			http_log_path=self.conf.DIRECTORIO_INSTALAR + "/logs/access.log",
			pid_path=self.conf.DIRECTORIO_INSTALAR + "run/nginx.pid",
			lock_path=self.conf.DIRECTORIO_INSTALAR + "lock/nginx.lock",
			http_client_body_temp_path=self.conf.DIRECTORIO_INSTALAR + "tmp/client/",
			http_proxy_temp_path=self.conf.DIRECTORIO_INSTALAR + "tmp/proxy/",
			http_fastcgi_temp_path=self.conf.DIRECTORIO_INSTALAR + "tmp/fcgi/"
		)


	def guarda_datos_instalacion(self):
		configuracion_instalacion_nginx  = {
			"directorio_temporal_instalacion": self.conf.TEMP,
			"directorio_temporal_instalacion_nginx": self.ruta_nginx,
			"version_nginx": self.conf.FILENAME,
			"configure_command_nginx": self.genera_configure(),
			"SUDO": self.conf.SUDO_ALL,
			"directorio_instalacion": self.conf.DIRECTORIO_INSTALAR
		}
		with open('configuraciones/configuracion.json', 'w') as f:
			json.dump(configuracion_instalacion_nginx, f)


#call(["wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'"], shell = True)

#call([" /home/zykor/"], shell = True)
#call(["pwd"], shell = True)


# wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'
# tar -xzf nginx-1.7.2.tar.gz
# cd nginx-1.7.2
# ./configure
# make
# sudo make install