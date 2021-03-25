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
    apt update && apt upgrade
    pkg install python -y
    pip install --upgrade pip
    pip install requests colorama
    pkg install dos2unix
    mkdir ~/.bomber
    cp ~/Sms-bomber/Unix/Sms-BomberSos2.2.py ~/.bomber
    chmod -R 777 ~/.bomber
    cp ~/.bomber/Sms-BomberSos2.2.py $PREFIX/bin/sayd123
    dos2unix $PREFIX/bin/sayd123
    clear
    echo "sayd123 - Вызов"
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
            apt install dos2unix
            mkdir ~/.bomber
            cp ~/Sms-bomber/Unix/Sms-BomberSos2.2.py ~/.bomber
            chmod -R 777 ~/.bomber
            cp ~/.bomber/Sms-BomberSos2.2.py $PREFIX/bin/sayd123
            dos2unix $PREFIX/bin/sayd123
            clear
            echo "sayd123 - Вызов"
        fi
    else
        if [ $numb = "3" ]
        then
            apk add python
            apk add python3
            apk add dos2unix
            pip3 install requests 
            pip3 install colorama
            mkdir ~/.bomber
            cp ~/Sms-bomber/Unix/Sms-BomberSos2.2.py ~/.bomber
            chmod -R 777 ~/.bomber
            cp ~/.bomber/Sms-BomberSos2.2.py $PREFIX/bin/sayd123
            dos2unix $PREFIX/bin/sayd123
            clear
            echo "sayd123 - Вызов"