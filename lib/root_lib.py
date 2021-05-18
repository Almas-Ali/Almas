import getpass
import os
from src.defpsd import *
from lib.STD_lib import *
from lib.ali_lib import *

if __name__ == '__main__':
    print('Use interpreter or get strick.')
    exit()

psd = ''


def root_mode(pmt):
    global psd
    try:
        if psd == defpsd:
            if pmt[0:4] == 'sudo':
                pmt = pmt[5:].strip()
                if pmt == '':
                    return None
                else:
                    try:
                        STD_lib(pmt)
                    except:
                        ali_lib(pmt)
            else:
                print('almas: sudo not found.')
        else:
            psd = getpass.getpass(prompt='Password: ', stream=None)
            if psd == defpsd:
                if pmt[0:4] == 'sudo':
                    pmt = pmt[5:].strip()
                    try:
                        STD_lib(pmt)
                    except:
                        try:
                            ali_lib(pmt)
                        except:
                            pass
                else:
                    print('almas: sudo not found.')
            else:
                print('Wrong Password !')
    except Exception as e:
        print(e)
