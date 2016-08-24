#-*- coding: utf-8 -*-
#Autor: Andrés Montoya (SpyRock)
#No me hago responsable del mal uso que este se le pueda dar.
#!/usr/bin/python
import sys
import os
from colores import *
class install(bcolors):
	def __init__(self):
		if not os.geteuid() == 0:
			sys.exit("""\033[1;91m\n[!] The Instalation Need Root Pemissions. ¯\_(ツ)_/¯\n\033[1;m""")
		else:
			os.system("cd .. && cd .. && mv ExpGenerator /opt/")
			os.system("cp expgenerator /usr/bin && chmod +x /usr/bin/expgenerator")
			
			print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Checking if Metasploit is installed...\n"
			if os.path.exists("/opt/metasploit-framework"):
				print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"True...!\n"
			else:
				print bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"False...!\n"
				MetasploitNoInstalled = raw_input(bcolors.payload+("Want to install metasploit? (y/n) "))
				if MetasploitNoInstalled == "y":
					print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Installing Metasploit...\n"
					os.system("chmod +x metasploit && ./metasploit")
				else:
					pass
			print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Checking if Apache is installed...\n"
			if os.path.exists("/var/www/html/"):
				print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"True...!"
			else:
				print bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Fail...!\n"
				apache = raw_input(bcolors.payload+"You want to install Apache? (y/n) ")
				if apache == "y":
					print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Installing Apache..."
					os.system("apt-get install apache2")
				else:
					pass
		print bcolors.WARNING+"\nInstallation Finished."
Iniciar = install()
