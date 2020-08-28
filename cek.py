#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
C1 = "\033[1;36m"
G0 = "\033[0;32m"
W0 = "\033[0;37m"
R0 = "\033[0;31m"
import requests,sys,os
from multiprocessing.pool import ThreadPool
def scan(web):
	try:
		cek=requests.get('http://'+web,timeout=10).url
		print '%s[%s>%s] %s'%(W0,G0,W0,cek)
		open('results.txt','a+').write(cek+'\n')
	except:
		pass
try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s
   ______________ __
  / ____/ ____/ //_/  %sCoded by D4RKSH4D0WS%s
 / /   / __/ / ,<     %sFB gg.gg/AnonRoz-Team%s
/ /___/ /___/ /| |    %sIG @anonroz_team%s
\____/_____/_/ |_|    SSL WEBSITE
	'''%(C1,W0,C1,W0,C1,W0,C1)
	ThreadPool(int(sys.argv[2])).map(scan,open(sys.argv[1]))
	print '\n%s[%s*%s] Done, saved in results.txt'%(W0,C1,W0)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W0,R0,W0,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 %s web-list.txt 30'%(W0,R0,W0,W0,sys.argv[0]))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W0,R0,W0,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W0,R0,W0,W0))
