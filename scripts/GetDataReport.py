# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                     #
# Modules   : GetDataReport   #
# Script by : RedToor         #
# Date      : 02/03/2015      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import help         #
from core import ping         #
import sys                    #
d=DESIGN()                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import socket                 #
import subprocess             #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                     #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultred="www.google.com"
defaultjav="true"
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(target, js):
	global defaultred,defaultjav
	defaultred=target
	defaultjav=js
	getdatareport(1)

def getdatareport(run):
	try:
		global defaultred,defaultjav
		if run!=1:
			actions=raw_input(d.prompt("set/gdreport"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("link","yes","redirectly",defaultred)
			d.descrip("java","no","JS for Geo",defaultjav)
 			d.space()
		elif actions[0:8] == "set link":
			defaultred=ping.update(defaultred,actions,"link")
			d.change("link",defaultred)
		elif actions[0:9] == "set javas":
			defaultjav = actions[10:]
			if defaultjav == "true" or defaultjav == "false":
				d.change("javas",defaultjav)
			else:
				d.nodataallow()
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				print " "+Alr+" Setting files",ping.status_cmd('echo "<?php \$url=\'http://'+defaultred+'\';\$javascript=\''+defaultjav+'\';?>" > '+PATCH_WWW+'/appconfig.php & echo ',"\t\t\t\t")
				print " "+Alr+" Coping files to server",ping.status_cmd("cp files/getdatareport/* "+PATCH_WWW,"\t\t\t")
				print " "+Alr+" Giving privileges to files",ping.status_cmd("chmod -R 777 "+PATCH_WWW,"\t\t")
				if True:
					try:
						print " "+Alr+" Starting Apache Server",ping.status_cmd("service apache2 start","\t\t\t")
						d.go("http://127.0.0.1/redirect.php?id=1337")
						raw_input(" "+Hlp+" Press any key for Stop GetDataReport")
						print(" "+Alr+" Stoping Process")
						print " "+Alr+" Removing files",ping.status_cmd("rm "+PATCH_WWW+"/redirect.php "+PATCH_WWW+"/appconfig.php "+PATCH_WWW+"/jquery.js","\t\t\t\t")
						print " "+Alr+" Stoping Apache",ping.status_cmd("service apache2 stop","\t\t\t\t")
					except:
						print ""
						print(" "+Alr+" Stoping Process")
						print " "+Alr+" Removing files",ping.status_cmd("rm "+PATCH_WWW+"/redirect.php "+PATCH_WWW+"appconfig.php "+PATCH_WWW+"/jquery.js","\t\t\t\t")
						print " "+Alr+" Stoping Apache",ping.status_cmd("service apache2 stop","\t\t\t\t")
						print ""
						getdatareport(0)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=False)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	getdatareport(0)
