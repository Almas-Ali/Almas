if __name__ =='__main__':
	print('Use interpreter or get strick.')
	exit()

import os, getpass, time, sys
from lib.root_lib import *
from lib.ali_lib import *
from src.defpsd import *

def STD_lib(pmt):
    global psd
    pmt.strip()
    if pmt == '':
    	return True
    elif pmt[0:5] == 'clear':
        pmt = pmt[5:].strip()
        try:
        	if pmt == '':
        		os.system('clear')
        	else:
        		print('almas: [Error] clearing screen ! ')
        except:
        	if pmt == '':
        		os.system('cls')
        	else:
        		print('almas: [Error] clearing screen !')
    elif pmt[0:3] == 'cls':
        pmt = pmt[3:].strip()
        try:
        	if pmt == '':
        		os.system('clear')
        	else:
        		print('almas: [Error] clearing screen ! ')
        except:
        	if pmt == '':
        		os.system('cls')
        	else:
        		print('almas: [Error] clearing screen !')
    elif pmt[:4] == 'exit':
    	pmt = pmt[4:].strip()
    	try:
    		intp.close()
    	except:
    		pass
    	if pmt == '':
    		sys.exit()
    	else:
    		print('almas: [Error] on exit function !')
    elif pmt[0:5] == 'print':
    	pmt = pmt[5:].strip()
    	if pmt == '':
    		print()
    	else:
    		print(pmt)
    elif pmt[0:2] == 'ls':
    	pmt = pmt[2:].strip()
    	if pmt =='':
    		os.system('ls')
    	else:
    		print('almas: [Error] ls don\'t take any command but given something !')
    elif pmt[0:3] == 'dir':
    	pmt = pmt[3:].strip()
    	if pmt == '':
    		os.system('ls')
    	else:
    		print('almas: [Error] dir don\'t take any command but given something !')
    elif pmt[0:3] == 'pwd':
    	pmt = pmt[3:].strip()
    	if pmt == '':
    		print(os.getcwd())
    	else:
    		print('almas: [Error] pwd don\'t take any command but given something !')
    elif pmt[0:5] == 'chdir':
    	pmt = pmt[5:].strip()
    	if pmt == '':
    		print('almas: [Error] chdir has no command.')
    	else:
    		try:
	    		os.chdir(pmt)
	    	except:
	    		print(f"almas: [Error] no directory found named \'{pmt[6:]}\'")
    elif pmt[0:2] == 'cd':
    	pmt = pmt[3:].strip()
    	if pmt == '':
    		print('almas: [Error] cd has no command.')
    	else:
    	 	try:
    	 		os.chdir(pmt)
    	 	except:
    	 		print(f"almas: [Error] no directory found named \'{pmt}\'")
    elif pmt[0:4] == 'calc':
    	pmt = pmt[5:].strip()
    	if pmt == '':
    		print('almas: [Error] calc has no command.')
    	else:
    		try:
    			print(eval(pmt))
    		except:
    			print("almas: [Error] takes only number to calculate.")
    elif pmt[0:4] == 'bash':
    	pmt = pmt[5:].strip()
    	if pmt == '':
    		print('almas: bash has no command.')
    	else:
    		try:
    			os.system(pmt)
    		except:
    			print(f"almas: [Error] no command exist named \'{pmt}\'")
    elif pmt.isnumeric() == 'True':
    	ba = str(pmt).strip()
    	ba = eval(ba)
    	print(ba)
    elif pmt[0:1] == '!':
    	if pmt[0:2] == '!!':
    		print(pmt[2:])
    	elif pmt[0:1] =='!':
    		print(pmt[1:].strip())
    elif pmt[0:4] == 'sudo':
    	root_mode(pmt)
    elif pmt[:6] == 'whoami':
    	if pmt[6:].strip() == '':
    		print(getpass.getuser())
    	else:
    		print('almas: [Error] on whoami function !')
    elif pmt[0:3] == 'ali':
    	ali_lib(pmt)
    elif pmt[0:3] == 'cat':
    	pmt = pmt[4:].strip()
    	if pmt == '':
    		print('almas: [Error] cat has no command.')
    	else:
    		try:
    			text = open(pmt).readlines()
    			for abc in text:
    				print(abc, end = '')
    		except:
    			print(f"almas: [Error] cat: \'{pmt}\' file not found !")
    elif pmt[0:4] == 'call':
    	pmt = pmt[5:].strip()
    	if pmt == '':
    		print('almas: no module name found to call.')
    	elif pmt[-3:] == '.al':
    		try:
	    		intp = open(pmt).readlines()
	    		for lex in intp:
	    			if lex == '\n':
	    				lex = ''
	    			elif lex == 'exit':
	    				print('yes')
	    				sys.exit()
	    			STD_lib(lex)
	    	except:
	    		print(f'almas: [Error] There is no file named \'{pmt}\'')
    	else:
    		print('It is not almas script ! ')
    elif pmt[0:1] == '#':
    	pmt = pmt[2:]
    	if pmt == '':
    		pass
    	else:
    		pass
    elif pmt[0:2] == '\\n':
    	pmt = pmt[3:].strip()
    	if pmt == '':
    		print()
    	else:
    		print()
    		STD_lib(pmt)
    elif pmt[0:5] == 'sleep':
    	pmt = str(pmt[6:]).strip()
    	if pmt == '':
    		print('almas: [Error] sleep has no command.')
    	else:
    		try:
    			pmt = int(pmt)
    			time.sleep(pmt)
    		except:
    			print('almas: [Error] sleep takes only integer number !')
    elif pmt[0:2] == '>>':
    	global defaulter
    	if pmt[2:].lstrip() == '':
    		defaulter = input()
    	else:
    		defaulter = input(pmt[2:])
    elif pmt[0:5] == 'input':
    	if pmt[6:].lstrip() == '':
    		defaulter = input()
    	else:
    		defaulter = input(pmt[6:])
    elif pmt[0:1] == '$':
    	try:
    		pmt[1:] = defaulter
    	except:
    		print('almas: no value been assigned')
    elif pmt[0:2] == '$$':
    	pmt = pmt[3:]
    	print(pmt)
    elif pmt[0:5] == 'about':
    	print('''
About - Almas Interpreter
    	
    	''')
    elif pmt[0:5] == 'almas':
    	print('''
Almas - Interpreter
version : 0.0.1

This language is made by Md. Almas Ali.
All the files and functions and all things been created my him.
He is the only author of this language.

© Copyright collected by Md. Almas Ali''')
    elif pmt == 'help':
    	print('''
Almas - Interpreter
version : 0.0.1

ali         - For managing packages.
bash        - For using bash commands
cls, clear  - For clearing console screen.
cd, chdir   - For changing current directory.
calc        - For calculating number.
cat         - For examine any source code.
dir         - For list of current directory elements.
exit        - For exiting the prompt.
help        - For showing help screen.
ls          - For list of current directory elements.
print       - For showing any text in the screen.
!           - For printing statements without prespaces.
!!          - For use with all spaces.
pwd         - For showinging current directory.
sudo        - For becoming Super User.
whoami      - For getting current user name.

Note: Default Root Password is 'toor'.

© Copyright collected by Md. Almas Ali''')
    else:
    	print("\""+pmt+"\"", "is not in any module of almas interpreter.")
