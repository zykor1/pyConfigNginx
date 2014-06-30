from pide_informacion import solicita_string, solicita_int, solicita_si_no
from ejecuta_comando import ejecutar_comando, get_from_terminal, get_home

DIRECTORIO_INSTALAR = get_home + "/server/nginx"

def configura_directorio():
	print "Por default nginx se instalara en: " + DIRECTORIO_INSTALAR
	if solicita_si_no("¿Deseas cambiar el directorio?"):
		DIRECTORIO_INSTALAR = solicita_string("¿Escribe la ruta absoluta donde lo deseas instalar?")



call(["wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'"], shell = True)

call([" /home/zykor/"], shell = True)
call(["pwd"], shell = True)


# wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'
# tar -xzf nginx-1.7.2.tar.gz
# cd nginx-1.7.2
# ./configure
# make
# sudo make install