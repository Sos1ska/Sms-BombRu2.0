try:
	import requests
except:
	print(f"У вас не установлен requests, для его установки введите pip install requests")
import services
import os
from colorama import Fore, Style
import time

def ban():
	print('''
░██████╗░█████╗░░██████╗░░███╗░░░██████╗██╗░░██╗░█████╗░░░░░░░██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░░██████╗
██╔════╝██╔══██╗██╔════╝░████║░░██╔════╝██║░██╔╝██╔══██╗░░░░░░██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔════╝
╚█████╗░██║░░██║╚█████╗░██╔██║░░╚█████╗░█████═╝░███████║█████╗███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝╚█████╗░
░╚═══██╗██║░░██║░╚═══██╗╚═╝██║░░░╚═══██╗██╔═██╗░██╔══██║╚════╝██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗░╚═══██╗
██████╔╝╚█████╔╝██████╔╝███████╗██████╔╝██║░╚██╗██║░░██║░░░░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║██████╔╝
╚═════╝░░╚════╝░╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░
	''')

def warn():
    print('''
.-----------------------.
|       Внимание        |
|-----------------------|
| Используйте VPN       |
| Для того чтобы не     |
| Не вводить постоянно  |
| Капчу "Анти-Бот"      |
'-----------------------'
	Данная версия находится в BETA-версии''')
warn()
time.sleep(5)
os.system("clear")
ban()
print(Fore.RED + '[Sos1ska-Bomber 2.1 RU - BETA]' + Style.RESET_ALL)

print("Tor не работает")
print()
print('Код написан им', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + 'https://vk.com/nikitasos1ska')

# Установка номера телефона, а также кол-во смс
print(Fore.YELLOW + 'Введите номер телефона. Пример:' + Style.RESET_ALL, Fore.CYAN + '+79021100147' + Style.RESET_ALL)
input_number = input(Fore.GREEN + ">> " + Style.RESET_ALL)
print(Fore.YELLOW + 'Кол-во смс?' + Style.RESET_ALL)
sms = int(input(Fore.GREEN + ">> " + Style.RESET_ALL))

# Преложение от СМС-атаки через Tor
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
		quit()
	return number
number = parse_number(input_number)

# Tor
if str(is_tor) == "Y":
	print(f"[*]Запускаю {Red}Tor{end}...")
	proxies = {
		'http': 'socks5://139.59.53.105:1080',
		'https': 'socks5://139.59.53.105:1080'
	}
	tor = requests.get('http://icanhazip.com/', proxies=proxies).text
	tor = (tor.replace('\n', ''))
	print(f"[*]Запуск Tor - Завершено. Вы в безопасности")

services.attack(number, sms)
