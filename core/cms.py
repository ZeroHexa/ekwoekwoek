import requests,time
from core.colornjinx import warna

class _cms():
	"""This Class For check the  initial"""
	def __init__(self):
		self.rs = requests.session()
		self.hd = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
		self.clr = warna()

	def _wordpress(self, url):
		
		wp_1 = self._curl(url)
		wp_2 = self._curl(url+'/license.txt')
		wp_3 = self._curl(url+'/xmlrpc.php?rsd')


		if wp_2.status_code == 200:
			if 'WordPress' in str(wp_2.text.encode('utf-8')):
				self.save(url, "Wordpress.txt")
				print(self.clr.green("[+] [Wordpress CMS] => {}".format(url)))
		elif wp_3.status_code == 200:
			if 'WordPress' in str(wp_3.text.encode('utf-8')):
				self.save(url, "Wordpress.txt")
				print(self.clr.green("[+] [Wordpress CMS] => {}".format(url)))
		elif wp_1.status_code == 200:
			if '/wp-content/' in str(wp_1.text.encode('utf-8')):
				self.save(url, "Wordpress.txt")
				print(self.clr.green("[+] [Wordpress CMS] => {}".format(url)))
		else:
			print(self.clr.red("[-] [NOT WORDPRESS] => {}".format(url)))

	def prestashop(self, url):

		prestashop = self._curl(url)
		clr = self.clr

		if prestashop.status_code == 200:
			if 'content="PrestaShop"' in str(prestashop.text.encode('utf-8')):
				self.save(url, "Prestashop.txt")
				print(self.clr.green("[+] [Prestashop CMS] => {}".format(url)))
		else:
			print(self.clr.red("[-] NOT PRESTASHOP {}".format(url)))

	def magento(self,url):
		magento = self._curl(url + '/user/login')
		magento2 = self._curl(url)

		if magento.status_code == 200:
			if 'magento' in str(magento2.text.encode('utf-8')) or 'Magento' in str(magento2.text.encode('utf-8')):
				self.save(url, "Magento.txt")
				print(self.clr.green("[+] [Magento CMS] => {}".format(url)))
		else:
			print(self.clr.red("[-] [NOT MAGENTO] {}".format(url)))
	def opencart(self,url):
		opencart = self._curl(url)

		if 'catalog/view/' in str(opencart.text.encode('utf-8')):
			self.save(url, "Opencart.txt")
			print(self.clr.green("[+] [Opencart CMS] => {}".format(url)))
		else:
			print(self.clr.red("[+] [NOT Opencart] => {}".format(url)))
			
	def _laravel(self,url):

		laravel = self._curl(url).headers
		if 'laravel_session' in str(laravel):
			print(self.clr.green("[+] [Laravel Framework] => {}".format(url)))
			self.save(url, "Laravel.txt")
		else:
			print(self.clr.red("[-] [NOT LARAVEL] {} ".format(url)))

	def _codeigniter(self,url):

		codeigniter = self._curl(url).headers
		if 'ci_session' in str(codeigniter):
			print(self.clr.green("[+] [Codeigniter Framework] => {}".format(url)))
			self.save(url, "Codeigniter.txt")
		else:
			print(self.clr.red("[-] [NOT CODEIGNITER] {} ".format(url)))

	def _curl(self,url):
		rc = self.rs

		try:
			url = rc.get(url,headers=self.hd, verify=False, timeout=100)
			return url
		except Exception as e:
			pass

	def _execute(self,url):

		rq = self._curl(url)

		if rq is not None:
			if rq.status_code == 200:
				self._wordpress(url)
				self.prestashop(url)
				self.magento(url)
				self.opencart(url)
				self._laravel(url)
				self._codeigniter(url)
			else:
				print(self.clr.red("[+] DEAD SITES {}".format(url)))
		else:
			print(self.clr.red("[+] SITES SOMETHING WRONG {}".format(url)))

	def save(self, sites, names):
		s = open(names, "a+")
		s.write(sites+"\n")

		return s



		