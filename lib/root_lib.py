if __name__ =='__main__':
	print('Use interpreter or get strick.')
	exit()
	
psd = ''

import os,getpass
from lib.ali_lib import *
from lib.STD_lib import *
from src.defpsd import *

def root_mode(pmt):
	global psd
	try:
	   if psd == defpsd:
	   	if pmt[0:4] == 'sudo':
	   		pmt = pmt[5:].strip()
	   		if pmt == '':
	   			return True
	   		else:
	   			try:
	   				STD_lib(pmt)
	   			except:
	   				ali_lib(pmt)
	   	else:
	   		print('almas: sudo not found.')
	   else:
	   	psd = getpass.getpass( prompt = 'Password: ', stream = None )
	   	if psd == defpsd:
	   		if pmt[0:4] == 'sudo':
	   			pmt = pmt[5:].strip()
	   			STD_lib(pmt)
	   		else:
	   			print('almas: sudo not found.')
	   	else:
	   		print('Wrong Password !')
	except Exception as e:
		print(e)
