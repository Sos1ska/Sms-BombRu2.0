clear
echo
echo ".-------------------------------------------."
echo "|                 Кто ты?                   |"
echo "| _________________________________________ |"
echo "|                                           |"
echo "| 1 - Termux                                |"
echo "| 2 - Другая UNIX система                   |"
echo "| 3 - iSH                                   |"
echo "|                                           |"
echo "'-------------------------------------------'"
echo
read numb
if [ $numb = "1" ]
then
    pkg install python
    pip install --upgrade pip
    pip install requests colorama
    clear
    echo "python3 Sms-BomberSos2.1.py"
else
    if [ $numb = "2" ]
    then
        if [ "$(whoami)" != 'root' ];
		then
			echo "У вас нет прав. Запустите install.sh с root правами (sudo sh ~/Spider-Breaking2.0/Unix/install.sh)"
			exit
        else
            apt install python3
            pip3 install requests colorama
            clear
            echo "python3 Sms-BomberSos2.1.py"
        fi
    else
        if [ $numb = "3" ]
        then
            apk add python
            apk add python3
            pip3 install requests 
            pip3 install colorama
            clear
            echo "python3 Sms-BomberSos2.1.py"