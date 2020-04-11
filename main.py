import sys,os.path,time,warnings,pyfiglet,os,requests
import re
from multiprocessing.dummy import Pool	
from time import time as timer
from core.cms import _cms
from core.colornjinx import warna
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore',InsecureRequestWarning)

cms = _cms()
clr = warna()


def main():
	out = pyfiglet.figlet_format("Find Me", font="alligator")
	print(clr.blue(out))
	a = input("Your list : ")
	c = input("Your Threads : ")
	threads = RepresentsInt(c)

	if threads == True:
		try:
			l = []
			with open(a, "r") as p:
				for x in p:
					l.append(formaturl(x.strip()))
		except IOError as e:
			print("[-] LIST NOT FOUND")
		pass
		victim = list((l))

		try:
			start = timer()
			ThreadPool = Pool(int(c))
			Threads = ThreadPool.map(cms._execute, victim)
			ThreadPool.close()
			ThreadPool.join()
			print('TIME TAKE: ' + str(timer() - start) + ' S')
		except Exception as e:
			pass

	else:
		print("[-] Only int or use number for Threads or 1 !")

def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url

def RepresentsInt(s):
    try: 
        if int(s) or int(s) > 0:
        	return True
    except ValueError:
        return False



if __name__ == '__main__':

	try:
		main()
	except KeyboardInterrupt as e:
		print("[!] Exiting Program")
		sys.exit()
	