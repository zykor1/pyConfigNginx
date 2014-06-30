# -*- coding: utf-8 -*-
TRUE = ["True", "si", "Si", "s", "S", "1", "Yes", "yes", "Y", "y", "true"]

def solicita_string(mensaje):
	res = raw_input(mensaje)
	return res

def solicita_int(mensaje):
	res = raw_input(mensaje)
	if res.isdigit():
		return int(res)
	return None

def solicita_si_no(mensaje):
	res = raw_input(mensaje)
	if res in TRUE:
		return True
	return False