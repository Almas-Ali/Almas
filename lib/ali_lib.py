if __name__ =='__main__':
	print('Use interpreter or get strick.')
	exit()

#from lib.root_lib import *
from src.defpsd import *
from src.ali_tool_info import *
import os, time

ali_help = '''
Ali - Package Manager For Almas Interpreter

update    - For updating source code and library.

© Copyright collected by Md. Almas Ali '''

def ali_lib(pmt):
	global psd
	pmt = pmt.strip()
	if pmt[0:3] == 'ali':
		pmt = pmt[4:].strip()
		if pmt == '':
			print(ali_help)
		elif pmt[0:7] == 'install':
			pmt = pmt[8:].strip()
			print(f"collecting information for \'{pmt}\'...")
			time.sleep(1)
			if pmt in tools:
				print('information collected.')
				time.sleep(1)
				print('preparing installation.')
			else:
				print(f"almas: ali: \'{pmt}\' information for this tool not found !")
		elif pmt == 'update':
			#if psd == defpsd:
			print('Updating Almas Interpreter...')
			#os.system('wget --help')
#			else:
#				print('You don’t have root permission.')
		else:
			print(f"almas: ali: \'{pmt}\' command not found !")
			print(ali_help)
			#print('Updating Failed.')
	else:
		print('almas: error calling ali !')
		